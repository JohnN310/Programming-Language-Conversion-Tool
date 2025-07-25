from mcp import ClientSession
from mcp.client.sse import sse_client
from CustomLLM import CustomLLM
from prompt import *
import asyncio
from scanner_client import customllm
import json

class ConverterClient:
    def __init__(self, folder_path, project_summary):
        self.folder_path = folder_path
        self.project_summary = project_summary

    async def convert(self):
        async with sse_client(url="http://localhost:8000/sse") as (read, write):
            async with ClientSession(read, write) as session:
                if hasattr(session, "initialize"):
                    await session.initialize()
                response = None
                file_content = await session.call_tool("concatenate_smalltalk_files", {"folder_path": self.folder_path})
                file_content = file_content.content[0].text
                prompt = (
                    "Here is your task:\n" +
                    converter_prompt +
                    "\nHere is the project summary for reference:\n" +
                    self.project_summary +
                    "\nHere is the original project code to be converted to java:\n" +
                    file_content
                )
                while True:
                    try:
                        response = customllm.generate_response(prompt=prompt)
                        response = json.loads(response)
                        break
                    except Exception as e:
                        print("Exception: ", e, " trying again...")
                return response

    def get_converted_code(self):
        return asyncio.run(self.convert())
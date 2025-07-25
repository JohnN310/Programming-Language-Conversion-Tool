from mcp import ClientSession
from mcp.client.sse import sse_client
from CustomLLM import CustomLLM
from prompt import *
import asyncio
from scanner_client import customllm
import json

class JuinitClient:
    def __init__(self, folder_path, project_summary, java_code_file_path):
        self.folder_path = folder_path
        self.project_summary = project_summary
        self.java_code_file_path = java_code_file_path

    async def junit(self):
        async with sse_client(url="http://localhost:8000/sse") as (read, write):
            async with ClientSession(read, write) as session:
                if hasattr(session, "initialize"):
                    await session.initialize()
                response = None
                test_file_content = await session.call_tool("concatenate_smalltalk_files_test", {"folder_path": self.folder_path})
                test_file_content = test_file_content.content[0].text

                java_code = await session.call_tool("load_file", {"folder_path": self.java_code_file_path})
                java_code = java_code.content[0].text

                prompt = (
                    "Here is your task:\n" +
                    junit_prompt +
                    "\nHere is the project summary for reference:\n" +
                    self.project_summary +
                    "\nHere is the converted java code:\n"+
                    java_code+
                    "\nHere is the unit tests from the original project:\n" +
                    test_file_content
                )
                while True:
                    try:
                        response = customllm.generate_response(prompt=prompt)
                        response = json.loads(response)
                        break
                    except Exception as e:
                        print("Exception: ", e, " trying again...")
                return response

    def get_junit(self):
        return asyncio.run(self.junit())
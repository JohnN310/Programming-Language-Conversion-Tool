from mcp import ClientSession
from mcp.client.sse import sse_client
from CustomLLM import CustomLLM
from prompt import *
import asyncio
from scanner_client import customllm

class DependencyClient:
    def __init__(self, java_code_file_path, project_summary):
        self.java_code_file_path = java_code_file_path
        self.project_summary = project_summary

    async def dependency(self):
        async with sse_client(url="http://localhost:8000/sse") as (read, write):
            async with ClientSession(read, write) as session:
                if hasattr(session, "initialize"):
                    await session.initialize()
                
                java_code = await session.call_tool("load_file", {"folder_path": self.java_code_file_path})
                java_code = java_code.content[0].text

                prompt = (
                    "Here is your task:\n" +
                    dependency_prompt +
                    "\nHere is the project summary for reference:\n" +
                    self.project_summary +
                    "\nHere is the converted java code that you are making the dependencies for:\n" +
                    java_code
                )
                response = customllm.generate_response(prompt=prompt)
                return response

    def get_dependency(self):
        return asyncio.run(self.dependency())
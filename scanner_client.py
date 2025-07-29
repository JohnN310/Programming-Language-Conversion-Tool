from mcp import ClientSession
from mcp.client.sse import sse_client
from CustomLLM import CustomLLM
from prompt import scanner_prompt
import asyncio

customllm = CustomLLM()
class ScannerClient:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    async def scan(self):
        async with sse_client(url="http://localhost:8000/sse") as (read, write):
            async with ClientSession(read, write) as session:
                if hasattr(session, "initialize"):
                    await session.initialize()
                file_content = await session.call_tool("concatenate_smalltalk_files", {"folder_path": self.folder_path})
                file_content = file_content.content[0].text
                prompt = (
                    scanner_prompt +
                    "\nHere is the original project code to be scanned:\n" +
                    file_content
                )
                response = customllm.generate_response(prompt=prompt)
                return response

    async def get_scanned(self):
        return await self.scan()
    
# scanner = ScannerClient(folder_path= "C:/Users/anhkh/Downloads/Github/Legacy Code Migration Tool/smalltalk_project")
# print(scanner.get_scanned())
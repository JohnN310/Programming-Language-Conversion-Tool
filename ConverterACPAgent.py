from collections.abc import AsyncGenerator

from acp_sdk.models import Message, MessagePart
from acp_sdk.server import RunYield, RunYieldResume, Server
from code_converter_client import *
server = Server()


@server.agent()
async def convert(inputs: list[Message]) -> AsyncGenerator[RunYield, RunYieldResume]:
    """LLM agent that processes inputs and returns a response"""

    folder_path, project_summary  = None, None 
    for message in inputs:
        for part in message.parts:
            if part.content_type == "folder_path":
                folder_path = part.content
            if part.content_type == "project_summary":
                project_summary = part.content

    java_code = await ConverterClient(folder_path= folder_path, project_summary= project_summary).get_converted_code()

    yield MessagePart(content= json.dumps(java_code), content_type= "java_code")


server.run(host="0.0.0.0", port=9001)
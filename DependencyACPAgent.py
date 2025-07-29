from collections.abc import AsyncGenerator

from acp_sdk.models import Message, MessagePart
from acp_sdk.server import RunYield, RunYieldResume, Server
from dependency_client import *
server = Server()


@server.agent()
async def dependency(inputs: list[Message]) -> AsyncGenerator[RunYield, RunYieldResume]:
    """LLM agent that processes inputs and returns a response"""

    java_code_file_path, project_summary  = None, None 
    for message in inputs:
        for part in message.parts:
            if part.content_type == "java_code_file_path":
                java_code_file_path = part.content
            if part.content_type == "project_summary":
                project_summary = part.content

    dependency = await DependencyClient(java_code_file_path= java_code_file_path, project_summary= project_summary).get_dependency()

    yield MessagePart(content=dependency, content_type= "dependency")


server.run(host="0.0.0.0", port=9002)
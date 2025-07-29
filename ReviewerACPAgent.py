from collections.abc import AsyncGenerator
import json
from acp_sdk.models import Message, MessagePart
from acp_sdk.server import RunYield, RunYieldResume, Server
from reviewer_client import *
server = Server()


@server.agent()
async def review(inputs: list[Message]) -> AsyncGenerator[RunYield, RunYieldResume]:
    """LLM agent that processes inputs and returns a response"""

    folder_path, java_code_file_path, project_summary  = None, None, None 
    for message in inputs:
        for part in message.parts:
            if part.content_type == "folder_path":
                folder_path = part.content
            if part.content_type == "java_code_file_path":
                java_code_file_path = part.content
            if part.content_type == "project_summary":
                project_summary = part.content

    review = await ReviewerClient(folder_path= folder_path, project_summary= project_summary, java_code_file_path= java_code_file_path).get_reviewer()

    yield MessagePart(content=json.dumps(review), content_type= "review")


server.run(host="0.0.0.0", port=9004)
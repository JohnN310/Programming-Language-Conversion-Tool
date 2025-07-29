from collections.abc import AsyncGenerator

from acp_sdk.models import Message, MessagePart
from acp_sdk.server import RunYield, RunYieldResume, Server
from scanner_client import *
server = Server()


@server.agent()
async def scanner(inputs: list[Message]) -> AsyncGenerator[RunYield, RunYieldResume]:
    """LLM agent that processes inputs and returns a response"""

    message_str = ""
    for message in inputs:
        message_str = str(message)

    project_summary = await ScannerClient(folder_path= message_str).get_scanned()

    yield MessagePart(content=project_summary, content_type= "project_summary")


server.run(host="0.0.0.0", port=9000)
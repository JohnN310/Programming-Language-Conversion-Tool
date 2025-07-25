from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP()

@mcp.tool()
def concatenate_smalltalk_files(folder_path): 
    smalltalk_content = ""   
    for filename in os.listdir(folder_path):
        filename = os.path.join(folder_path, filename)
        if os.path.isfile(filename) and filename.endswith(".st") and 'test' not in filename.lower():
            with open(filename, 'r') as f:
                smalltalk_content += f.read()
    return smalltalk_content

@mcp.tool()
def concatenate_smalltalk_files_test(folder_path): 
    smalltalk_content = ""   
    for filename in os.listdir(folder_path):
        filename = os.path.join(folder_path, filename)
        if os.path.isfile(filename) and filename.endswith(".st") and 'test' in filename.lower():
            with open(filename, 'r') as f:
                smalltalk_content += f.read()
    return smalltalk_content

@mcp.tool()
def load_file(folder_path):
    with open(folder_path, 'r') as f:
        read = f.read()
    return read

if __name__ == "__main__":
    mcp.run(transport= "sse")
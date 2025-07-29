import asyncio

from acp_sdk.client import Client
from acp_sdk.models import Message, MessagePart
import json
import os 
import streamlit as st
import shutil


async def main() -> None:
    st.title("Smalltalk to Java Conversion Tool")
    folder_path = st.text_input("Paste your project path here: ")
    if st.button("Run"):
        async with Client(base_url="http://localhost:9000") as scanner_agent:
            run = await scanner_agent.run_sync(
                agent="scanner",
                input=[
                    Message(parts=[MessagePart(content=folder_path, content_type="text/plain")])
                ],
            )
            project_summary = None
            if run.output:
                for msg in run.output:
                    for part in msg.parts:
                        if part.content_type == "project_summary":
                            project_summary = part.content

        st.header("Project Summary")
        st.markdown(project_summary)


        async with Client(base_url="http://localhost:9001") as converter_agent:
            run = await converter_agent.run_sync(
                agent="convert",
                input=[
                    Message(parts=[MessagePart(content=folder_path, content_type="folder_path")]),
                    Message(parts=[MessagePart(content=project_summary, content_type="project_summary")])
                ],
            )
            java_code = None
            if run.output:
                for msg in run.output:
                    for part in msg.parts:
                        if part.content_type == "java_code":
                            java_code = part.content

        java_code = json.loads(java_code)
        base_path_main = os.path.join( os.path.dirname(folder_path), "src/main/java")
        os.makedirs(base_path_main, exist_ok=True)
        st.header("Converted Code")
        keys = java_code["java_code"].keys()
        if os.path.exists("java_code.md"):
            with open("java_code.md", "w") as f:
                f.write("")
        for key in keys:
            st.markdown(f"Code for {key}")
            st.code(java_code["java_code"][key])
            with open("java_code.md", "a") as f:
                f.write(f"// {key}\n")
                f.write(java_code["java_code"][key])
                f.write("\n\n")
            full_path = os.path.join(base_path_main, key)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(java_code["java_code"][key])
        

        async with Client(base_url="http://localhost:9002") as dependency_agent:
            run = await dependency_agent.run_sync(
                agent="dependency",
                input=[
                    Message(parts=[MessagePart(content="java_code.md", content_type="java_code_file_path")]),
                    Message(parts=[MessagePart(content=project_summary, content_type="project_summary")])
                ],
            )
            dependency = None
            if run.output:
                for msg in run.output:
                    for part in msg.parts:
                        if part.content_type == "dependency":
                            dependency = part.content        
        st.header("Maven Dependencies")
        st.code(dependency)
        base_path_resources = os.path.join(os.path.dirname(folder_path), "src/main/resources")
        os.makedirs(base_path_resources, exist_ok= True)
        full_path_resources = os.path.join(base_path_resources, "pom.xml")
        with open(full_path_resources, 'w') as f:
            f.write(dependency)


        async with Client(base_url="http://localhost:9003") as junit_agent:
            run = await junit_agent.run_sync(
                agent="junit",
                input=[
                    Message(parts=[MessagePart(content=folder_path, content_type="folder_path")]),
                    Message(parts=[MessagePart(content="java_code.md", content_type="java_code_file_path")]),
                    Message(parts=[MessagePart(content=project_summary, content_type="project_summary")])
                ],
            )
            junit_tests = None
            if run.output:
                for msg in run.output:
                    for part in msg.parts:
                        if part.content_type == "junit":
                            junit_tests = part.content
        junit_tests = json.loads(junit_tests)
        base_path_test = os.path.join(os.path.dirname(folder_path), "src/test/java")
        os.makedirs(base_path_test, exist_ok= True)
        st.header("JUnit Tests")
        junit_keys = junit_tests.keys()
        for key in junit_keys:
            st.markdown(f"Code for {key}")
            st.code(junit_tests[key])
            full_path_test = os.path.join(base_path_test, key)   
            with open(full_path_test, 'w') as f:
                f.write(junit_tests[key])


        async with Client(base_url="http://localhost:9004") as reviewer_agent:
            run = await reviewer_agent.run_sync(
                agent="review",
                input=[
                    Message(parts=[MessagePart(content=folder_path, content_type="folder_path")]),
                    Message(parts=[MessagePart(content="java_code.md", content_type="java_code_file_path")]),
                    Message(parts=[MessagePart(content=project_summary, content_type="project_summary")])
                ],
            )
            review = None
            if run.output:
                for msg in run.output:
                    for part in msg.parts:
                        if part.content_type == "review":
                            review = part.content   
        review = json.loads(review)
        st.header("Performance Evaluation")
        st.subheader("Score (out of 100)")
        st.markdown(review["score"])
        st.subheader("Justification")
        st.markdown(review["justification"])
        st.subheader("Suggestions")
        st.markdown(review["improvement"])
        score = review["score"]    

        # hallucination checks
        counter = 3
        while score < 96 and counter > 0: 
            counter -= 1
            st.header("Re-converted Java code")
            updated_project_summary = "The generated java code wasn't good enough, consider the project summary and regenerate the java code.\n" + project_summary + "\n In addition, consider the following improvement: " + review["improvement"]
            async with Client(base_url="http://localhost:9001") as converter_agent:
                run = await converter_agent.run_sync(
                    agent="convert",
                    input=[
                        Message(parts=[MessagePart(content=folder_path, content_type="folder_path")]),
                        Message(parts=[MessagePart(content=updated_project_summary, content_type="project_summary")])
                    ],
                )
                java_code = None
                if run.output:
                    for msg in run.output:
                        for part in msg.parts:
                            if part.content_type == "java_code":
                                java_code = part.content

            java_code = json.loads(java_code)
            base_path_main = os.path.join( os.path.dirname(folder_path), "src/main/java")
            if os.path.exists(base_path_main):
                shutil.rmtree(base_path_main)
            os.makedirs(base_path_main, exist_ok=True)
            st.subheader("Converted Code")
            keys = java_code["java_code"].keys()
            if os.path.exists("java_code.md"):
                with open("java_code.md", "w") as f:
                    f.write("")
            for key in keys:
                st.markdown(f"Code for {key}")
                st.code(java_code["java_code"][key])
                with open("java_code.md", "a") as f:
                    f.write(f"// {key}\n")
                    f.write(java_code["java_code"][key])
                    f.write("\n\n")
                full_path = os.path.join(base_path_main, key)
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(java_code["java_code"][key])

            async with Client(base_url="http://localhost:9004") as reviewer_agent:
                run = await reviewer_agent.run_sync(
                    agent="review",
                    input=[
                        Message(parts=[MessagePart(content=folder_path, content_type="folder_path")]),
                        Message(parts=[MessagePart(content="java_code.md", content_type="java_code_file_path")]),
                        Message(parts=[MessagePart(content=updated_project_summary, content_type="project_summary")])
                    ],
                )
                review = None
                if run.output:
                    for msg in run.output:
                        for part in msg.parts:
                            if part.content_type == "review":
                                review = part.content   
                review = json.loads(review)
                score = review["score"] 
                st.subheader("Evaluation score")
                st.markdown(score)


if __name__ == "__main__":
    asyncio.run(main())
import google.generativeai as genai
import os
import streamlit as st
from CustomLLM import CustomLLM

from scanner_client import ScannerClient
from code_converter_client import ConverterClient
from dependency_client import DependencyClient
from junit_client import JuinitClient

st.title("Smalltalk to Java Conversion Tool")
folder_path = st.text_input("Paste your project path here: ")
if st.button("Run"):
    project_summary = ScannerClient(folder_path= folder_path).get_scanned()
    st.header("Project Summary")
    st.markdown(project_summary)

    converted_code = ConverterClient(folder_path= folder_path, project_summary= project_summary).get_converted_code()
    base_path_main = os.path.join( os.path.dirname(folder_path), "src/main/java")
    os.makedirs(base_path_main, exist_ok=True)
    st.header("Converted Code")
    keys = converted_code["java_code"].keys()
    if os.path.exists("java_code.md"):
        with open("java_code.md", "w") as f:
            f.write("")
    for key in keys:
        st.markdown(f"Code for {key}")
        st.code(converted_code["java_code"][key])
        with open("java_code.md", "a") as f:
            f.write(f"// {key}\n")
            f.write(converted_code["java_code"][key])
            f.write("\n\n")
        full_path = os.path.join(base_path_main, key)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(converted_code["java_code"][key])

    dependency = DependencyClient(java_code_file_path="java_code.md", project_summary= project_summary).get_dependency()
    st.header("Maven Dependencies")
    st.code(dependency)
    base_path_resources = os.path.join(os.path.dirname(folder_path), "src/main/resources")
    os.makedirs(base_path_resources, exist_ok= True)
    full_path_resources = os.path.join(base_path_resources, "pom.xml")
    with open(full_path_resources, 'w') as f:
        f.write(dependency)

    junit_tests = JuinitClient(folder_path= folder_path, project_summary= project_summary, java_code_file_path="java_code.md").get_junit()
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
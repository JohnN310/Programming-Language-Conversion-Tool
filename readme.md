# Smalltalk to Java Conversion Tool

## Overview
This project provides an **AI-driven legacy modernization tool** that automates the conversion of **Smalltalk code to Java**, enabling enterprises to upgrade outdated systems while reducing technical debt.  

Developed with an **Agentic AI architecture**, this solution allows the **FSSTAR unit at Infosys** to efficiently modernize legacy applications with minimal manual intervention.

---

## Key Features
- **Smalltalk to Java Conversion:**  
  Automatically translates Smalltalk code into Java, preserving logic and structure.

- **Agentic AI Approach:**  
  A network of **4 specialized AI agents** work collaboratively to handle every step of the migration process:
  1. **Code Scanning Agent** – Extracts and analyzes Smalltalk source files.  
  2. **Translation Agent** – Converts Smalltalk syntax and constructs into Java.  
  3. **Dependency Generation Agent** – Produces Maven dependencies (`pom.xml`).  
  4. **JUnit Test Generation Agent** – Generates test cases for the new Java code.

- **Model Context Protocol (MCP):**  
  Establishes shared project context for better translation accuracy.

- **Agent Communication Protocol (ACP):**  
  Agents collaborate autonomously to perform scanning, translation, and evaluation in a pipeline.

- **Modular and Extensible Design:**  
  Can be extended to support additional languages in future legacy modernization initiatives.

---

## Technology Stack
- **Python** (backend automation and AI orchestration)
- **Streamlit** (for interactive UI)
- **OpenAI GPT Models** (translation engine)
- **Model Context Protocol (MCP)** & **A2A communication** (agent orchestration)
- **Maven** (for managing dependencies)
- **JUnit** (for automated test generation)

---

## How It Works
1. **Code Scanning:**  
   The scanning agent reads Smalltalk source files and extracts key classes, methods, and logic.

2. **Translation:**  
   The translation agent converts Smalltalk classes, methods, and control structures into equivalent Java code.

3. **Dependency Generation:**  
   A `pom.xml` is generated with required Maven dependencies.

4. **Testing:**  
   The JUnit agent creates test cases to validate the translated Java code.

5. **Evaluating**
    The Reviewer agent performs a deep evaluation on the other agents' performance. 

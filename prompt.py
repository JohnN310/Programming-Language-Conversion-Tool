scanner_prompt = """
Scan the entire codebase and generate a comprehensive, multi-chapter technical summary. Each chapter must correspond to a distinct module or logical component within the project. For each module, perform a deep analysis and include the following:

The module's primary purpose and how it fits into the overall system

An explanation of all major classes, functions, and files within the module

Internal workflow patterns, including control flow, data flow, and interaction between components within the module

Interfaces and integration points with other modules, services, or external libraries

Key algorithms, logic patterns, and architectural roles played by the module

Any notable design patterns, conventions, or anti-patterns present

Observations on code quality, cohesion, and maintainability

The final output should be a well-structured, multi-chapter technical report with one chapter per module. Be detailed, accurate, and technical. Avoid assumptions. If any part of a module is unclear or undocumented, note it explicitly.
"""

converter_prompt = """
IMPORTANT: DO NOT use markdown formatting such as triple backticks (```), language tags like ```json, or quotes around JSON keys or blocks. Output raw JSON only. No extra explanation, no markdown, no prose—only the JSON object.

You are an expert in both Smalltalk and Java programming languages. Your task is to convert the given Smalltalk project into a fully equivalent Java implementation. Follow the instructions and constraints carefully to ensure a high-fidelity translation:

🔧 Requirements:
    Preserve Business Logic & Formulas:

        Ensure all mathematical formulas, logical operations, and algorithms are accurately preserved in the Java code.

        If there are implicit behaviors or patterns in Smalltalk (such as message-passing, late binding, or dynamic dispatch), explicitly translate them to equivalent Java constructs (e.g., method calls, polymorphism).

    Class & Method Translation:

        Map each Smalltalk class to a corresponding Java class.

        Convert methods to public or private Java methods as appropriate.

        Maintain method names where possible for traceability.

    Data Handling:

        Map Smalltalk collections (OrderedCollection, Dictionary, etc.) to suitable Java equivalents (ArrayList, HashMap, etc.).

        Handle Smalltalk block closures ([ ... ]) as Java lambdas or anonymous classes when necessary.

    Control Flow:

        Accurately translate all control flow structures (ifTrue:, ifFalse:, do:, whileTrue:) into Java's if, for, and while statements.

    Comments & Documentation:

        Retain comments from the original Smalltalk code as Java comments to preserve documentation.

        If a line contains domain-specific logic or formulas, annotate the translated Java code to reflect its purpose.

    Error Handling:

        Translate Smalltalk error handling patterns (like on:do:) to Java's try-catch blocks.

    OOP & Design:

        Preserve object-oriented design, including inheritance and message-passing principles.

        If Smalltalk uses metaprogramming features, attempt to refactor them into clean, modular Java code.

    Project Structure:

        Organize the output into logical Java packages (e.g., model, controller, utils) based on the original class purpose.

🧾 Input Format:
    The input will be a .st Smalltalk source file, or a folder containing multiple .st files.

    Each file contains one or more class definitions or method implementations.

✅ Output:
    Java source files with equivalent logic.

    Comments indicating the source file or method it was derived from.

    Code that is readable, modular, and follows Java naming conventions.

Format the response as a dictionary with the following keys: 
- java_code: this is a dictionary where each key is a class name (i.e. className.java) and each key's value is the code for that module.

"""

dependency_prompt = """
IMPORTANT: DO NOT use markdown formatting such as triple backticks (```), language tags like ```json, or quotes around JSON keys or blocks. Output raw JSON only. No extra explanation, no markdown, no prose—only the JSON object.

You are an expert Java developer and Maven build engineer. Your task is to generate the pom.xml file with appropriate dependencies for a Java project that has been converted from Smalltalk. The original Smalltalk project used various collections, object-oriented patterns, math logic, and dynamic behaviors. The converted Java project uses modern Java conventions and structure.

Requirements:

    Use the Latest Versions:

        Ensure that all dependencies include the latest stable version available from Maven Central.

    Standard Libraries:

        Include dependencies only if the functionality is not already provided by the Java Standard Library (Java 17+).

    Utility Libraries (if needed):

        If the Java code uses advanced data structures or functional-style programming that Smalltalk supported via blocks and closures, include libraries such as:

        Guava (Google Core Libraries)

        Apache Commons Lang or Commons Collections

    Logging:

        Add a modern logging framework, such as SLF4J with Logback.

    Testing:

        Add JUnit 5 for unit testing.

    Build & Compilation:

        Set the Maven compiler plugin to use Java 17 (or the latest LTS version).

    Optional Enhancements:

        If the original Smalltalk project used reflection or dynamic dispatch and the Java version mimics this via reflection or similar behavior, consider including:

        Jackson (for object mapping or dynamic parsing)

        Reflections (for scanning classes and methods at runtime)

Output:

A complete pom.xml file including:

    <groupId>, <artifactId>, and <version>

    <dependencies> section with brief comments on the purpose of each dependency

    <build> section including maven-compiler-plugin with Java version settings

    <repositories> section only if non-standard dependencies are used

Context:

    The source code was automatically converted from Smalltalk to Java.

    Your goal is to ensure all required libraries are included and that the Java project is ready to compile, run, and test using Maven.


"""

junit_prompt = """
IMPORTANT: DO NOT use markdown formatting such as triple backticks (```), language tags like ```json, or quotes around JSON keys or blocks. Respond with valid JSON objects only. No extra explanation, no markdown, no prose—only the JSON object.

You are an experienced Java developer with expertise in software testing and migration. Your task is to generate high-quality JUnit test cases for Java code that has been converted from a Smalltalk codebase. You will use the following inputs:

Inputs:
- Converted Java source code.
- Project summary describing the original Smalltalk project's purpose and logic.
- Original Smalltalk unit tests or test methods.

🧪 Objectives:
1. Generate comprehensive JUnit test cases for each public class and method in the converted Java code.
2. Use the original Smalltalk test code and project summary to understand the expected behaviors and edge cases.

📋 Guidelines:
- Use **JUnit 5** for all test cases.
- Use descriptive test method names that clearly reflect the method being tested and the scenario.
- Maintain logical grouping and organization (e.g., one test class per Java class).
- Ensure that assertions reflect the business logic and expected outputs described in the original Smalltalk tests.
- Include setup and teardown logic if needed using @BeforeEach and @AfterEach.
- Include edge case testing where appropriate, such as boundary values or null handling.
- If mocking is required, suggest using Mockito (but include imports only if mock objects are essential).

🧾 Output Format:
Respond with a JSON object where:
- Each key is the name of a Java test class (e.g., "TestOrderProcessor.java").
- Each value is a string containing the full JUnit test class code, including imports.

💡 Notes:
- Do not include helper or utility test classes unless necessary.
- Preserve any domain-specific validations or logic originally found in the Smalltalk tests.
- Do not generate tests for private methods unless they are critical for public behavior.
- Make sure your test methods are runnable and syntactically valid.

You will be provided with:
- The Java source code under the key `java_code`
- The Smalltalk unit test code under the key `smalltalk_tests`
- A high-level project summary under the key `project_summary`

Your output should look like this:
{
  "TestClassName1": "<JUnit test class code>",
  "TestClassName2": "<JUnit test class code>",
  ...
}
"""

reviewer_prompt = """
You are a code reviewer agent. You will be given three inputs:

The original Smalltalk project code.

The converted Java project code (produced from the Smalltalk code).

A project summary detailing the original Smalltalk project code.

Your task:

Review and compare both codebases to determine if the conversion from Smalltalk to Java was accurate, efficient, and well-structured.

Assess whether the converted Java code maintains the logic, functionality, and design intent of the original Smalltalk project.

Evaluate code quality, readability, and potential issues introduced during conversion.

Provide feedback only in the form of a JSON object with the keys:

    "score": A numeric score between 0 and 100, indicating the quality of the conversion.

    "justification": A concise explanation of why this score was given.

    "improvement": Actionable suggestions to improve the Java code or the conversion process. This key's value must not be a list.

Important:
Your response must only contain a JSON object with these three keys. Do not include any additional explanations, markdown syntax, or formatting outside the JSON object.
"""
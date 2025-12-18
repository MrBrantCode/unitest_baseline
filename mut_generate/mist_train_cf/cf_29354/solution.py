"""
QUESTION:
Write a function `create_environment` that takes a string of space-separated lowercase letters and returns a formatted string. The function should split the input string into individual components, capitalize each component, and format them into a list with bullet points. The output should start with "Environment Components:" followed by a newline character, and each component should be on a new line.
"""

def create_environment(input_str):
    components = input_str.split()
    formatted_environment = "Environment Components:\n"
    for component in components:
        formatted_environment += f"- {component.capitalize()}\n"
    return formatted_environment
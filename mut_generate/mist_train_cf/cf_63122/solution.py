"""
QUESTION:
Implement a function called `remove_debug_statements` that takes a code string as input and removes the lines that are used for debugging purposes, marked by a specific annotation. The function should return the modified code string without the debug statements. The function should be able to handle different types of annotations and languages.
"""

def remove_debug_statements(code_string, annotation="#debug"):
    """
    Removes the lines that are used for debugging purposes, 
    marked by a specific annotation from the given code string.

    Args:
        code_string (str): The input code string.
        annotation (str, optional): The annotation used to mark debug statements. Defaults to "#debug".

    Returns:
        str: The modified code string without the debug statements.
    """
    lines = code_string.split('\n')
    cleaned_lines = [line for line in lines if annotation not in line]
    return '\n'.join(cleaned_lines)
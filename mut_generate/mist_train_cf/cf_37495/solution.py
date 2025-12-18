"""
QUESTION:
Write a function `extract_code_snippets(input_string: str) -> List[str]` that takes in a string `input_string` containing multiple Python code snippets enclosed within triple quotes (`"""..."""`) and returns a list of all the code snippets in the order they appear. Assume the input string contains valid Python code snippets with no nested triple quotes within the snippets.
"""

from typing import List

def extract_code_snippets(input_string: str) -> List[str]:
    snippets = []
    start_index = 0
    while True:
        start_index = input_string.find('"""', start_index)
        if start_index == -1:
            break
        end_index = input_string.find('"""', start_index + 3)
        if end_index == -1:
            break
        snippet = input_string[start_index + 3:end_index].strip()
        snippets.append(snippet)
        start_index = end_index + 3
    return snippets
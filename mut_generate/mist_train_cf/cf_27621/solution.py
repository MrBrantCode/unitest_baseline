"""
QUESTION:
Implement the function `findMissingBrace` that takes a string `code` as input, where the code contains a portion of a program with a missing opening or closing brace for a while loop, and the missing brace is the only missing character in the code. The function should return the missing brace, either "{" or "}".
"""

def findMissingBrace(code: str) -> str:
    brace_count = 0
    for char in code:
        if char == '{':
            brace_count += 1
        elif char == '}':
            brace_count -= 1
    if brace_count < 0:
        return "{"
    else:
        return "}"
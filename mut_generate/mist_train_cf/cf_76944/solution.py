"""
QUESTION:
Write a function called `interpreter_step` that takes a string representing a line of code as input and returns a string describing the steps an interpreter would take to execute that line of code, including reading, parsing, semantic analysis, and execution. The function should assume the input code is syntactically correct and semantically valid.
"""

def interpreter_step(code):
    return f"""
    The interpreter reads: {code}
    The interpreter parses: {code}
    The interpreter performs semantic analysis on: {code}
    The interpreter executes: {code}
    """
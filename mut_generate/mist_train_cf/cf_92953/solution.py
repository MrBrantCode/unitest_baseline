"""
QUESTION:
Write a function called `identify_syntax_errors` that takes a string of Python code as input and identifies any syntax errors. The function should use the Python `compile()` function and catch `SyntaxError` exceptions to report any syntax errors found in the code.
"""

def identify_syntax_errors(code):
    try:
        compiled_code = compile(code, '<string>', 'exec')
        return "No syntax errors found!"
    except SyntaxError as e:
        return "SyntaxError: " + str(e)
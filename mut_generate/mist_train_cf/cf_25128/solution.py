"""
QUESTION:
Write a function `check_syntax` that takes a string of Python code as input and returns `True` if the code has a syntax error, and `False` otherwise. The input string can contain a single function definition.
"""

def check_syntax(code):
    try:
        compile(code, '<string>', 'exec')
        return False
    except SyntaxError:
        return True
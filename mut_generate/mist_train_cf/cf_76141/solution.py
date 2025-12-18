"""
QUESTION:
Write a function to verify if a given code snippet has any syntax errors that could prevent it from running. The function should take a string containing the code snippet as input and return a boolean indicating whether the code is syntactically correct.
"""

def verify_syntax(code):
    try:
        compile(code, '<string>', 'exec')
        return True
    except SyntaxError:
        return False
"""
QUESTION:
Write a function called `greet` that takes two parameters, `name` and `age`, and returns a greeting message. The function should handle the following cases:

- If `name` is not provided or is an empty string, return 'Hello, my friend!'.
- If `age` is not provided or is not a positive integer, return 'Invalid age provided!'.
- If `name` consists of uppercase letters only, return the greeting message in all uppercase letters.
- For any other cases, capitalize the first letter of the `name` parameter and return the greeting message.
"""

def greet(name, age):
    if not name or name == '':
        return 'Hello, my friend!'
    elif age <= 0 or not isinstance(age, int):
        return 'Invalid age provided!'
    elif name.isupper():
        return f'HELLO, {name}!'
    else:
        return f'Hello, {name.capitalize()}!'
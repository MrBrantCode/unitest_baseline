"""
QUESTION:
Create a `greet` function with a default parameter `name` set to an empty string. The function should return a personalized greeting message. If the `name` parameter is not provided or is an empty string, the function should return "Hello, my friend!". Otherwise, it should return a greeting message with the provided `name`.
"""

def greet(name: str = "") -> str:
    if not name:
        return "Hello, my friend!"
    return f"Hello, {name}!"
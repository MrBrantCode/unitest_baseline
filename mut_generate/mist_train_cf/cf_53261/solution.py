"""
QUESTION:
Write a function `greet` that takes a `name` parameter and returns a greeting message. The `name` parameter should be a string and the function should return a string. Implement type hinting for the `name` parameter and the return type of the function. Additionally, include error handling to raise an `AssertionError` if the `name` parameter is not a string.
"""

def greet(name: str) -> str:
    """
    Returns a greeting message for the given name.

    Args:
        name (str): The name to include in the greeting.

    Returns:
        str: A greeting message.
    """
    assert isinstance(name, str), f"Expected a string, but got {type(name).__name__}"
    return 'Hello, ' + name
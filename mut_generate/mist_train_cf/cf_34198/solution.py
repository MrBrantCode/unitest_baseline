"""
QUESTION:
Write a function `manipulate_string` that takes a string `name` (1 <= len(name) <= 1000) consisting of lowercase and uppercase letters, underscores, and digits as input, converts it to lowercase, replaces all underscores with spaces, and capitalizes the first letter of each word. The function should return the manipulated string.

The function should adhere to the following signature: `def manipulate_string(name: str) -> str:`
"""

def entrance(name: str) -> str:
    name = name.lower()
    name = name.replace('_', ' ')
    name = name.title()
    return name
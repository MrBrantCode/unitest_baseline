"""
QUESTION:
Create a function `reverseResponse` that takes a string `response` as input, where `response` is a series of words separated by spaces, and returns a modified version of `response` with the order of the words reversed while preserving the order of characters within each word and ensuring only one space between each word.
"""

def reverseResponse(response: str) -> str:
    return ' '.join(response.split()[::-1])
"""
QUESTION:
Formulate a new string by reassembling all the unique characters from a provided text in an inverse sequence, excluding spaces and disregarding character repetition. Upper-case and lower-case versions of the same alphabet are regarded as distinct characters. Implement the function `reverse_unique_chars(text: str) -> str` that takes a string as input and returns a string as output, following these rules.
"""

def reverse_unique_chars(text: str) -> str:
    result = ""
    for char in reversed(text):
        if char != " " and char not in result:
            result += char
    return result
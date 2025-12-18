"""
QUESTION:
Write a function `remove_numbers` that takes a document string as input and returns the modified document with all numbers removed. The function should have a time complexity of O(n), where n is the number of characters in the document, and use only O(1) space. The input document can contain up to 10^6 characters and any printable ASCII characters.
"""

def remove_numbers(document):
    result = ""
    for char in document:
        if not char.isdigit():
            result += char
    return result
"""
QUESTION:
Write a function `remove_numbers(document)` that takes a document string as input and returns the document with all numbers removed. The function should have a time complexity of O(n), where n is the number of characters in the document, and use only O(1) space. The document can contain any printable ASCII characters, including punctuation marks and special characters.
"""

def remove_numbers(document):
    result = ""
    for char in document:
        if not char.isdigit():
            result += char
    return result
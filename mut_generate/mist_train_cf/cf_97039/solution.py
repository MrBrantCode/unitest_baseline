"""
QUESTION:
Create a function `remove_numbers` that takes a string `document` as input and returns a modified string with all numbers removed. The function should have a time complexity of O(n), where n is the number of characters in the document, and should use only O(1) space. The input document can contain any printable ASCII characters, including punctuation marks and special characters, as well as numbers with leading or trailing whitespaces.
"""

def remove_numbers(document):
    modified_document = ""
    for ch in document:
        if not ch.isdigit():
            modified_document += ch
    return modified_document
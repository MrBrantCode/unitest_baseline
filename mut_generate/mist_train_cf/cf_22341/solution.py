"""
QUESTION:
Remove all numbers from a given document with up to 10^6 characters, handling cases where numbers have leading or trailing whitespaces. The solution should have a time complexity of O(n), where n is the number of characters in the document, and use only O(1) space. Implement the function `remove_numbers(document)` that takes the document as input and returns the modified document with all numbers removed.
"""

def remove_numbers(document):
    modified_document = ""
    for ch in document:
        if not ch.isdigit():
            modified_document += ch
    return modified_document
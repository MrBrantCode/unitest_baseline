"""
QUESTION:
Create a function named `process` that takes a single argument of any type. The function should return the argument processed according to its type: 
- If the argument is a string, return the reversed string.
- If the argument is a list, return the list in reversed order.
- If the argument is a dictionary, return a new dictionary with keys and values swapped.

The function will be used to process a list containing exactly four elements: two strings, a list, and a dictionary.
"""

def process(item):
    if isinstance(item, str):
        return item[::-1]
    elif isinstance(item, list):
        return item[::-1]
    elif isinstance(item, dict):
        return {v: k for k, v in item.items()}
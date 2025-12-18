"""
QUESTION:
Create a function called `convert_and_sort_string` that takes a string as input and returns a list of characters, where each character is represented as a string, sorted in descending order.
"""

def convert_and_sort_string(s):
    return sorted([str(char) for char in list(s)], reverse=True)
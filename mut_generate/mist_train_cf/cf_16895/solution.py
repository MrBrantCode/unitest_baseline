"""
QUESTION:
Create a function named `get_character` that takes a string and an index as input and returns the character at the given index in the string. The index must be a non-negative integer and within the range of the string length. If the index is out of range, the function should return an error message. The function should have a time complexity of O(1) and a space complexity of O(1).
"""

def get_character(string, index):
    length = len(string)
    if index >= 0 and index < length:
        return string[index]
    else:
        return "Error: Index out of range"
"""
QUESTION:
Create a function named `check_index` that takes a string `st` and an integer `index` as input. The function should return the character at the specified index if it exists, otherwise, it should return a message indicating that the index is out of range. The function should handle strings of any length and indices of any value, assuming Python's 0-based indexing.
"""

def check_index(st, index):
    if index < len(st):
        return st[index]
    else:
        return f"Index {index} is out of range for the string '{st}'"
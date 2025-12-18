"""
QUESTION:
Create a function `get_character` that takes a string and a non-negative integer index as input, and returns the character at the given index in the string. The function should have a time complexity of O(1) and a space complexity of O(1). It should not use any built-in string manipulation functions or data structures and only use basic operations such as indexing, arithmetic, and comparison operations. The function should not modify the original string or create any new strings, and should handle Unicode characters and support multibyte character encodings. If the index is out of range, the function should return an error message.
"""

def get_character(string, index):
    if index < 0 or index >= len(string):
        return "Error: Index out of range"

    left = 0
    right = len(string) - 1

    while left <= right:
        mid = (left + right) // 2

        if mid == index:
            return string[mid]
        elif mid > index:
            right = mid - 1
        else:
            left = mid + 1

    return "Error: Index out of range"
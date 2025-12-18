"""
QUESTION:
Implement a function named `reverse_string` that takes a string as input and returns the reversed string without using any built-in string reversal functions or methods. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1). The function should be able to handle string inputs containing special characters, whitespace, and Unicode characters, and it should not use any additional data structures or arrays.
"""

def reverse_string(string):
    string = list(string)  # Convert the string to a list of characters
    start = 0
    end = len(string) - 1

    while start < end:
        # Swap characters at start and end positions
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1

    return "".join(string)  # Convert the list back to a string
"""
QUESTION:
Write a function `reverse_string` that takes a string as input and returns the reversed string. The function should have a time complexity of O(n), where n is the length of the string, and should not use any built-in string manipulation functions or methods, or any additional data structures beyond a constant amount of extra memory.
"""

def reverse_string(string):
    string_list = list(string)  # convert the string to a list of characters
    start = 0
    end = len(string_list) - 1

    while start < end:
        # swap characters at start and end positions
        string_list[start], string_list[end] = string_list[end], string_list[start]
        start += 1
        end -= 1

    # convert the list of characters back to a string
    return "".join(string_list)
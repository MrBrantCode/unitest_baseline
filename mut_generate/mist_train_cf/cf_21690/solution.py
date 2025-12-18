"""
QUESTION:
Write a function called `reverse_string` that takes a string `s` as input and returns the reversed string without using any built-in string reverse functions. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the string.
"""

def reverse_string(s):
    # Convert the string to a list since strings in Python are immutable
    s = list(s)
    start = 0
    end = len(s) - 1

    while start < end:
        # Swap characters at start and end pointers
        s[start], s[end] = s[end], s[start]
        # Increment start pointer and decrement end pointer
        start += 1
        end -= 1

    # Convert the list back to a string
    return ''.join(s)
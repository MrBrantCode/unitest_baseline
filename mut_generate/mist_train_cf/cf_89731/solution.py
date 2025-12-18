"""
QUESTION:
Write a function called `reverse_string(s)` that takes a string `s` as input, reverses the characters in it without using any built-in reverse functions or extra memory, and returns the reversed string. The function should handle strings that contain special characters such as punctuation marks and whitespace.
"""

def reverse_string(s):
    start = 0
    end = len(s) - 1

    # Convert the string to a list since strings are immutable in Python
    s = list(s)

    while start < end:
        # Swap characters at start and end pointers
        s[start], s[end] = s[end], s[start]

        # Move pointers
        start += 1
        end -= 1

    # Convert the list back to a string
    return ''.join(s)
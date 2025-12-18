"""
QUESTION:
Write a function named `reverse_string` that takes a list of characters and two indices (start and end) as input, and reverses the characters in the list in place, without using any additional variables or data structures. The function should not return any value, but should modify the input list directly.
"""

def reverse_string(string, start, end):
    if start >= end:
        return
    # Swap the first and last characters
    string[start], string[end] = string[end], string[start]
    # Reverse the remaining characters
    reverse_string(string, start+1, end-1)
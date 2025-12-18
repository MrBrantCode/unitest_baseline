"""
QUESTION:
Write a function named `reverse_string` that takes a string `s` as input and reverses it in-place without using any additional data structures. The function should have a time complexity of O(n), where n is the length of the string.
"""

def entance(s):
    start = 0
    end = len(s) - 1

    # Loop until start is no longer less than end
    while start < end:
        # Swap characters at start and end pointers
        s[start], s[end] = s[end], s[start]

        # Increment start and decrement end
        start += 1
        end -= 1

    return s
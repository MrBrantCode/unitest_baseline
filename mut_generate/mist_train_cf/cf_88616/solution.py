"""
QUESTION:
Design a function `reverse_string` that takes a string as input and reverses the order of its alphanumeric characters in place without using any additional variables or data structures, while ignoring non-alphanumeric characters. The function should have a time complexity of O(n), where n is the length of the string, and handle strings with Unicode characters and special characters correctly.
"""

def reverse_string(s):
    # Convert the string into a list of characters
    s = list(s)

    # Initialize two pointers, one at the start and one at the end of the string
    start = 0
    end = len(s) - 1

    # Swap characters from both ends until the pointers meet in the middle
    while start < end:
        # Ignore special characters and whitespace by moving the pointers
        if not s[start].isalnum():
            start += 1
        elif not s[end].isalnum():
            end -= 1
        else:
            # Swap the characters
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    # Convert the list of characters back into a string
    return ''.join(s)
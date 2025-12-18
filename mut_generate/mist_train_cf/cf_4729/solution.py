"""
QUESTION:
Design a function named `reverse_string` that takes a string as input and returns the string with its alphanumeric characters reversed in place. The function should handle strings with special characters, whitespace, and Unicode characters correctly, and it should not use any additional variables or data structures to store the reversed string. The time complexity of the function should be O(n), where n is the length of the string.
"""

def reverse_string(string):
    # Convert the string into a list of characters
    string = list(string)

    # Initialize two pointers, one at the start and one at the end of the string
    start = 0
    end = len(string) - 1

    # Swap characters from both ends until the pointers meet in the middle
    while start < end:
        # Ignore special characters and whitespace by moving the pointers
        if not string[start].isalnum():
            start += 1
        elif not string[end].isalnum():
            end -= 1
        else:
            # Swap the characters
            string[start], string[end] = string[end], string[start]
            start += 1
            end -= 1

    # Convert the list of characters back into a string
    return ''.join(string)
"""
QUESTION:
Write a function called `longest_consecutive_string` that takes a string as input and returns the length of the longest consecutive substring without repeating characters. The function should only consider consecutive characters, not the entire substring, to check for repetition.
"""

def longest_consecutive_string(string):
    if len(string) == 0:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, len(string)):
        if string[i] != string[i-1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 1

    if current_length > max_length:
        max_length = current_length

    return max_length
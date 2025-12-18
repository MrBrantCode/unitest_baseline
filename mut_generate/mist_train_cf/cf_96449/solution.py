"""
QUESTION:
Write a function `longest_consecutive_string` that takes a string as input and returns the length of the longest consecutive string of non-repeating characters. The function should consider only sequences of distinct adjacent characters, resetting the count whenever it encounters a repeating character.
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
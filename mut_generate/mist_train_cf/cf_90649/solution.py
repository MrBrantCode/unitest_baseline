"""
QUESTION:
Create a function `longest_consecutive_sequence(string)` that returns the longest consecutive sequence of characters in a given string. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the string.
"""

def longest_consecutive_sequence(string):
    if len(string) == 0:
        return ""

    max_start = 0
    max_length = 1
    current_start = 0
    current_length = 1

    for i in range(1, len(string)):
        if ord(string[i]) == ord(string[i-1]) + 1:
            current_length += 1
        else:
            if current_length > max_length:
                max_start = current_start
                max_length = current_length

            current_start = i
            current_length = 1

    if current_length > max_length:
        max_start = current_start
        max_length = current_length

    return string[max_start:max_start+max_length]
"""
QUESTION:
Write a function called `longest_consecutive_sequence` that takes a string as input and returns the longest consecutive sequence of characters. The function must have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string. If there are multiple sequences with the same maximum length, return any of them.
"""

def longest_consecutive_sequence(string):
    if len(string) == 0:
        return ""

    max_start = 0
    max_length = 1
    current_start = 0
    current_length = 1

    for i in range(1, len(string)):
        if string[i] == string[i-1]:
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
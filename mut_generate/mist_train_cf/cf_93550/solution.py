"""
QUESTION:
Write a function `find_longest_string` that takes a list of strings and returns the longest string. The function must not use any built-in string manipulation functions or sorting algorithms. The time complexity should be O(n^2), where n is the total number of characters in all the strings combined, and the space complexity should be constant.
"""

def find_longest_string(strings):
    longest = ""
    max_length = 0

    for string in strings:
        length = 0
        for character in string:
            length += 1

        if length > max_length:
            max_length = length
            longest = string

    return longest
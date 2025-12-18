"""
QUESTION:
Design a function `find_longest_string` that takes a list of strings and returns the longest string without using any built-in string manipulation functions or sorting algorithms. The function should have a time complexity of O(n^2), where n is the total number of characters in all the strings combined, and should use constant space complexity.
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
"""
QUESTION:
Write a function `count_different_chars(str1, str2)` that takes two strings `str1` and `str2` as input, each of length at most 10^6 characters, and returns the number of characters that are different between the two strings. The function should handle strings containing any printable ASCII characters, including special characters, spaces, punctuation marks, and non-alphanumeric characters. The time complexity of the solution should be O(n), where n is the length of the strings.
"""

def count_different_chars(str1, str2):
    count = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            count += 1
    count += abs(len(str1) - len(str2))  # Account for any extra characters in one of the strings
    return count
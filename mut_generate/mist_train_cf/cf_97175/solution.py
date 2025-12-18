"""
QUESTION:
Write a function named `count_different_chars` that takes two text strings `str1` and `str2` as input. The function should return the number of characters that are different between the two strings, excluding spaces, considering characters with different case as different. The function should compare alphanumeric characters only, ignore special characters, and only consider characters up to the length of the shorter string for comparison.
"""

def count_different_chars(str1, str2):
    count = 0
    for char1, char2 in zip(str1, str2):
        if char1.isalnum() and char2.isalnum():
            if char1 != char2:
                count += 1
        elif char1 != char2:
            count += 1
    return count
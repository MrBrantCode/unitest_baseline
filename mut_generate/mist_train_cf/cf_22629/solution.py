"""
QUESTION:
Write a function named `count_different_chars` that takes two text strings as input and returns the difference between them. The function should only consider alphanumeric characters and spaces, ignore case differences, and only compare characters up to the length of the shorter string. The output should be the total number of different characters and spaces between the two strings.
"""

def count_different_chars(str1, str2):
    count = 0
    for char1, char2 in zip(str1.lower(), str2.lower()):
        if char1.isalnum() or char1.isspace():
            if char1 != char2:
                count += 1
    return count
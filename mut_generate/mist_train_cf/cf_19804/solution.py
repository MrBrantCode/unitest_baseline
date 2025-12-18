"""
QUESTION:
Write a function `remove_duplicates(input_string)` that takes a string as input and returns the string with all duplicate characters removed and the remaining characters sorted in ascending order, without using any extra space. The function must modify the input string in-place.
"""

def remove_duplicates(input_string):
    chars = list(input_string)
    chars.sort()
    i = 1
    j = 1
    while i < len(chars):
        if chars[i] != chars[i-1]:
            chars[j] = chars[i]
            j += 1
        i += 1
    del chars[j:]
    return "".join(chars)
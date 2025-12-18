"""
QUESTION:
Write a function `check_substring` that takes a string as input and returns the starting index of the first substring that contains all 26 English alphabets in consecutive order. If no such substring exists, return -1.
"""

def check_substring(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    index = 0

    for char in s:
        if char == alphabet[index]:
            index += 1
        if index == len(alphabet):
            return s.index(char) - (len(alphabet) - 1)

    return -1
"""
QUESTION:
Write a function `check_substring(string)` that checks if a given string contains all the alphabets in a specific order, consecutively, and in the same order as they do in the English alphabet. The function should return the starting index of the substring that satisfies the condition. If no such substring exists, return -1.
"""

def check_substring(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    index = 0

    for char in string:
        if char == alphabet[index]:
            index += 1
        if index == len(alphabet):
            return string.index(char) - (len(alphabet) - 1)

    return -1
"""
QUESTION:
Write a function `find_last_occurrence` that takes two parameters: a string and a character. The function should return the index of the last occurrence of the character in the string. If the character does not exist in the string, the function should return -1. You can only use basic string operations and looping constructs to solve this problem, and the solution should have a time complexity of O(n), where n is the length of the string.
"""

def find_last_occurrence(string, character):
    last_index = -1
    for i in range(len(string)):
        if string[i] == character:
            last_index = i
    return last_index
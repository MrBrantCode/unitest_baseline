"""
QUESTION:
Create a function `count_characters` that takes a string as input and returns a dictionary where the keys are the characters in the string and the values are the counts of each character. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity that is proportional to the number of unique characters in the string.
"""

def count_characters(string):
    char_counts = {}

    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts
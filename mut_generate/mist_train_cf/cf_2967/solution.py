"""
QUESTION:
Construct a function named `count_characters` that takes a string as input and returns a dictionary with the alphanumeric characters as keys and their respective counts as values. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(k), where k is the number of unique alphanumeric characters in the string. Non-alphanumeric characters should be excluded from the dictionary.
"""

def count_characters(string):
    char_counts = {}
    for char in string:
        if char.isalnum():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts
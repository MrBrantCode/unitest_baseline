"""
QUESTION:
Construct a Python function named `character_counts` that accepts an array of strings and returns a nested dictionary. The outer dictionary's keys should be the individual strings from the array. Each key's value should be another dictionary with keys as the unique characters from the string and values as the counts of those characters.
"""

def character_counts(arr):
    result = {}
    for word in arr:
        char_dict = {}
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
            else: 
                char_dict[char] = 1
        result[word] = char_dict
    return result
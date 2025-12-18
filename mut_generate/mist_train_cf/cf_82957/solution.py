"""
QUESTION:
Write a function `character_count(string)` that creates a case-insensitive dictionary from a given ASCII string where each character (including alphabets, punctuation, and numerical characters) serves as dictionary keys, and their respective repetition count within the string serves as the assigned dictionary values.
"""

def character_count(string):
    count_dict = {}
    for char in string.lower():
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict
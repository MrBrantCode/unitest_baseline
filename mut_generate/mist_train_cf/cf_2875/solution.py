"""
QUESTION:
Write a function `count_characters` that takes an input string of up to 10 million characters as input and returns a dictionary where each key is a character from the string and its corresponding value is the count of its occurrence. The function should efficiently handle special characters, whitespace, and punctuation marks as separate keys. The time complexity should be O(n), where n is the length of the input string.
"""

def count_characters(input_string):
    character_counts = {}
    
    for char in input_string:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    
    return character_counts
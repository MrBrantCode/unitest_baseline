"""
QUESTION:
Create a function named `character_count` that takes a list of strings as an argument. The function should return two values: the total number of characters in all the strings together and the number of unique characters in all the strings. The function should use a set data structure to keep track of unique characters.
"""

def character_count(input_list):
    total_chars = 0
    total_unique_chars = set()
    for sentence in input_list:
        total_chars += len(sentence)
        for char in sentence:
            total_unique_chars.add(char)
    return total_chars, len(total_unique_chars)
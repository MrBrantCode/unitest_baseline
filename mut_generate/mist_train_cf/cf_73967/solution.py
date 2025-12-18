"""
QUESTION:
Implement a function `extract_advanced_data(input_string)` that takes a string as input and returns a dictionary with the following rules: 

- If the input string contains a comma (`,`), split the string into words separated by commas and return a dictionary where each key is a word and its value is the occurrence of that word.
- If the input string contains a colon (`:`) but no comma, split the string into words separated by colons and return a dictionary where each key is a word and its value is the occurrence of that word.
- If the input string contains neither a comma nor a colon, treat the string as a sequence of characters where a character's index is its position in the alphabet (a=1, b=2, etc.), and return a dictionary where each key is an odd-indexed character and its value is the occurrence of that character. 

Restrictions: The function should handle any string input and return a dictionary.
"""

def extract_advanced_data(input_string):
    if ',' in input_string:
        split_sequence = input_string.split(',')
        return {word: split_sequence.count(word) for word in set(split_sequence)}
    elif ':' in input_string:
        split_sequence = input_string.split(':')
        return {word: split_sequence.count(word) for word in set(split_sequence)}
    else:
        odd_indexed_chars = [char for char in input_string if (ord(char.lower()) - ord('a')) % 2 == 1]
        return {char: input_string.count(char) for char in set(odd_indexed_chars)}
"""
QUESTION:
Create a function named `char_count` that accepts two strings, `string_1` and `string_2`, and returns a dictionary where each key represents a unique character from both strings. The value for each key should be a tuple where the first element is the count of that character's occurrence in `string_1` and the second element is the count in `string_2`. If a character does not appear in one of the strings, the count should be 0.
"""

def char_count(string_1, string_2): 
    return {char: (string_1.count(char), string_2.count(char)) for char in set(string_1+string_2)}
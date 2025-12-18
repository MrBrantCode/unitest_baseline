"""
QUESTION:
Create a function called `count_chars` that takes a string of lowercase alphabetic characters as input and returns a dictionary where the keys are the characters and the values are the corresponding character counts. Then create a function called `print_char_count` that takes this dictionary and prints the characters and their counts in descending order of occurrence count.
"""

def count_chars(input_string: str) -> dict:
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
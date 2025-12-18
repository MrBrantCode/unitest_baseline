"""
QUESTION:
Create a function named `char_count` that takes two parameters: an input string and a string of characters. The function should count the occurrences of each character in the input string, ignoring case sensitivity and punctuation, and return a dictionary with each character and its count. The function should only consider alphabetic characters.
"""

from collections import defaultdict
import string

def char_count(input_string, chars):
    input_string = input_string.lower()
    char_count_dict = defaultdict(int)
    for char in chars.lower():
        if char in string.ascii_lowercase:
            char_count_dict[char] = input_string.count(char)
    return char_count_dict
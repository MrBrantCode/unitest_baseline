"""
QUESTION:
Write a function named `get_letter_frequency` that calculates the frequency distribution of letters in a given string. The function should exclude non-alphabetic characters, treat uppercase and lowercase letters as separate entities, and include non-Latin characters. It should achieve this with a time complexity of O(n), where n is the length of the input string, and a space complexity that does not grow with the size of the input, excluding the space needed for the output.
"""

import string

def get_letter_frequency(string):
    frequency = {}
    for char in string:
        if char.isalpha():
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency
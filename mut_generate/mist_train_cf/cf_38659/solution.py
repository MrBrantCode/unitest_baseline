"""
QUESTION:
Create a function `character_frequency` that takes a string as input and returns a dictionary where the keys are the unique alphabetic characters in the input string and the values are the frequency of each character, ignoring case sensitivity and non-alphabetic characters. The function should consider only alphabetic characters in the input string.
"""

def character_frequency(input_string):
    frequency_dict = {}
    for char in input_string:
        if char.isalpha():
            char = char.lower()
            if char in frequency_dict:
                frequency_dict[char] += 1
            else:
                frequency_dict[char] = 1
    return frequency_dict
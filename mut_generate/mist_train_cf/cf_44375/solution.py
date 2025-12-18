"""
QUESTION:
Design a function named `letter_frequency` that takes a string input and returns a dictionary. The dictionary keys should be each unique character present in the string, including letters, punctuation marks, and spaces, and the values should be the frequency of each character.
"""

def letter_frequency(paragraph):
    frequency_dict = {}
    for char in paragraph:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return frequency_dict
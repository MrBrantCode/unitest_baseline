"""
QUESTION:
Implement the function `calculate_character_frequency` that calculates the frequency of each alphabetic character in a given string, ignoring case sensitivity and non-alphabetic characters. The function should take a string as input and return a dictionary where the keys are the alphabetic characters and the values are their frequencies, sorted in descending order of the characters' ASCII values. The function should handle edge cases such as an empty string, where the output dictionary should be empty.
"""

def calculate_character_frequency(string):
    frequency = {}
    for char in string:
        if char.isalpha():
            char = char.upper()
            frequency[char] = frequency.get(char, 0) + 1
    return dict(sorted(frequency.items(), key=lambda x: -ord(x[0])))
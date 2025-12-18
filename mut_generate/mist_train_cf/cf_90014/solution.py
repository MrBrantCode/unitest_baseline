"""
QUESTION:
Write a function called `calculate_character_frequency` that takes a string as input and returns a dictionary containing the frequency of each alphabet character in the string, ignoring case sensitivity and non-alphabet characters. The output dictionary should be sorted in descending order of the characters' ASCII values. If the input string is empty, the function should return an empty dictionary.
"""

def calculate_character_frequency(string):
    frequency = {}
    for char in string:
        if char.isalpha():
            char = char.upper()
            frequency[char] = frequency.get(char, 0) + 1
    return dict(sorted(frequency.items(), key=lambda x: -ord(x[0])))
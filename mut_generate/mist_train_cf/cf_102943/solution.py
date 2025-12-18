"""
QUESTION:
Create a function named `letter_frequency` that takes a string as input and returns a dictionary where the keys are the unique consonants in the string and the values are their corresponding frequencies. The function should be case-insensitive and ignore any non-alphabetic characters.
"""

def letter_frequency(string):
    frequency = {}
    string = string.lower()
    for char in string:
        if char not in "aeiou" and char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
    return frequency
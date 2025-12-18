"""
QUESTION:
Write a function `count_character_frequency` that takes a string as input, calculates the frequency of each alphabetic character (ignoring case), and returns the frequencies in alphabetical order. The function should only consider alphabetic characters and disregard non-alphabetic characters and case sensitivity.
"""

def count_character_frequency(user_input):
    frequency = {}
    for char in user_input:
        if char.isalpha():
            char = char.lower()
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

    return dict(sorted(frequency.items()))
"""
QUESTION:
Write a function `calculate_frequency` that takes a string `input_string` as input and returns a dictionary where the keys are the distinct characters in the string (excluding white spaces) and the values are their corresponding frequencies. The function should consider case sensitivity and punctuation.
"""

def calculate_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char != ' ':
            frequency[char] = frequency.get(char, 0) + 1
    return frequency
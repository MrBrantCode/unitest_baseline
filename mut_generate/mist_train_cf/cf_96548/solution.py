"""
QUESTION:
Write a function `get_string_length_and_frequency` that takes a string as input and returns a tuple containing the length of the string, the number of unique characters in the string, and a dictionary where the keys are the unique characters and the values are their respective frequencies. Do not use any built-in functions to calculate the string length. The function should handle strings containing special characters and spaces.
"""

def get_string_length_and_frequency(string):
    length = 0
    unique_chars = set()
    frequency = {}

    for char in string:
        if char not in unique_chars:
            unique_chars.add(char)
            frequency[char] = 1
        else:
            frequency[char] += 1

        length += 1

    return length, len(unique_chars), frequency
"""
QUESTION:
Write a function `find_most_repeated_char(input_string)` that takes a string `input_string` as input and returns the most repeated character in the string, considering special characters and blank spaces as valid characters and treating lower-case and upper-case variants of a character as distinct characters. The function should handle strings with multiple characters having the same maximum frequency by returning any of the characters.
"""

def find_most_repeated_char(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return max(frequency, key=frequency.get)
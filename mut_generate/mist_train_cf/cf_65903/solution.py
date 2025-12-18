"""
QUESTION:
Write a function `max_frequency_character(s)` that takes a string `s` as input and returns the most frequent character in the string along with its frequency. If multiple characters have the same highest frequency, return the lexicographically smaller one. The function should not use any built-in functions or methods related to frequency counts.
"""

def max_frequency_character(s):
    frequency = {}
    max_freq = 0
    max_char = ''

    # Find frequency count for each character
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Find maximum frequency character
    for char in sorted(frequency):
        if frequency[char] > max_freq:
            max_freq = frequency[char]
            max_char = char

    return max_char, max_freq
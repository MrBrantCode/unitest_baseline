"""
QUESTION:
Create a function `char_frequency` that takes a string as input, calculates the frequency of each alphabetic character while ignoring case sensitivity and non-alphabetic characters, and returns a dictionary sorted in descending order based on the frequency of the characters.
"""

def char_frequency(text):
    # Removing non-alphabetic characters and converting all characters to lowercase
    clean_text = ''.join(c for c in text if c.isalpha()).lower()

    # Creating a dictionary to store character frequencies
    char_freq = {}

    # Counting the frequency of each character
    for char in clean_text:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    # Sorting the dictionary in descending order based on frequency
    return {k: v for k, v in sorted(char_freq.items(), key=lambda item: item[1], reverse=True)}
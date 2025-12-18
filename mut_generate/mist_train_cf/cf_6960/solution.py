"""
QUESTION:
Create a function named `most_frequent_char` that takes a string as input and returns the most frequent alphabetic character in the string, ignoring case, punctuation, numbers, and whitespace. If multiple characters have the same highest frequency, return the character that appears first in the input string.
"""

def most_frequent_char(string):
    # Convert the string to lowercase and remove all punctuation, numbers, and whitespace
    cleaned_string = ''.join(char.lower() for char in string if char.isalpha())

    # Create a dictionary to store the frequency of each character
    frequency = {}

    # Iterate through the cleaned string and count the frequency of each character
    for char in cleaned_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Find the character with the highest frequency
    max_frequency = 0
    most_frequent_char = ''
    for char in frequency:
        if frequency[char] > max_frequency:
            max_frequency = frequency[char]
            most_frequent_char = char

    return most_frequent_char
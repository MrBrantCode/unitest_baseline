"""
QUESTION:
Create a function called `most_frequent_char` that takes a string as input, calculates the most frequent character (excluding punctuation, numbers, and whitespace, and considering both uppercase and lowercase characters as the same), and returns this character. If there are multiple characters with the same highest frequency, return the character that appears first in the input string. The function should not take any other parameters besides the input string.
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
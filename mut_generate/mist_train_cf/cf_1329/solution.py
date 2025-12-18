"""
QUESTION:
Write a function `most_frequent_character(string)` that returns the most frequent character in the given string, ignoring case sensitivity and considering alphanumeric characters, spaces, and special characters. If multiple characters have the same frequency, return the one that appears first in the string. The function should handle large input strings efficiently.
"""

def most_frequent_character(string):
    # Convert the string to lowercase for case-insensitive counting
    string = string.lower()
    
    # Create a dictionary to store the frequency of each character
    frequency = {}
    
    # Iterate through the string and update the count for each character
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    # Find the character with the maximum frequency
    max_frequency = 0
    most_frequent_char = ''
    for char, count in frequency.items():
        if count > max_frequency:
            max_frequency = count
            most_frequent_char = char
    
    # Return the most frequent character
    return most_frequent_char
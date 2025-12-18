"""
QUESTION:
Write a function named `most_frequent_character` that takes a string as input and returns the most frequent character in the string. The function should ignore the case sensitivity of characters when counting their frequencies. If multiple characters have the same frequency, return the one that appears first in the string. The input string will contain alphanumeric characters (lowercase and uppercase), spaces, and special characters. The function should handle large input strings efficiently.
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
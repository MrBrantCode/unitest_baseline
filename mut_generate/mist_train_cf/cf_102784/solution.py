"""
QUESTION:
Write a function `most_frequent_character` that returns the most frequent character in the given string. If there are multiple characters with the same frequency, return the one that appears first in the string. The function should take one parameter: `string`, the input string from which to find the most frequent character.
"""

def most_frequent_character(string):
    frequency = {}
    
    # Count the frequency of each character in the string
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    max_frequency = 0
    most_frequent_char = ''
    
    # Find the character with the highest frequency
    for char in string:
        if frequency[char] > max_frequency:
            max_frequency = frequency[char]
            most_frequent_char = char
    
    return most_frequent_char
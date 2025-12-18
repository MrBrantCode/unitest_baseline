"""
QUESTION:
Write a function called `find_highest_frequency_character` that takes a string as input and returns the character with the highest frequency in the string. If there are multiple characters with the same highest frequency, return the character that comes first in the string. The input string can contain alphanumeric characters, spaces, and special characters.
"""

def find_highest_frequency_character(string: str) -> str:
    frequency_dict = {}
    
    for char in string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    
    max_frequency = 0
    highest_frequency_character = ""
    
    for char, frequency in frequency_dict.items():
        if frequency > max_frequency:
            max_frequency = frequency
            highest_frequency_character = char
        elif frequency == max_frequency and string.index(char) < string.index(highest_frequency_character):
            highest_frequency_character = char
    
    return highest_frequency_character
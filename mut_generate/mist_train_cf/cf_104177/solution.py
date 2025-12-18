"""
QUESTION:
Write a function `most_frequent_character` that takes a string of alphabetic characters and spaces as input, and returns the most frequent character in the string, ignoring case sensitivity. If there are multiple characters with the same frequency, return the one that appears first in the string.
"""

def most_frequent_character(string):
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()
    
    # Create a dictionary to store the frequency of each character
    char_count = {}
    
    # Iterate through each character in the string
    for char in string:
        # Ignore spaces
        if char != ' ':
            # Increment the count of the character in the dictionary
            char_count[char] = char_count.get(char, 0) + 1
    
    # Find the character with the highest frequency
    max_freq = max(char_count.values())
    most_frequent = [char for char, freq in char_count.items() if freq == max_freq]
    
    # Return the first character with the highest frequency
    return most_frequent[0]
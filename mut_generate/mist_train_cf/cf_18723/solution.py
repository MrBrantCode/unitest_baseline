"""
QUESTION:
Write a function `count_characters(string)` that takes a string as input, counts the occurrences of each character in the string while ignoring the case of alphabetic letters, and returns the counts. The function should handle strings containing special characters, spaces, and digits, treating them as unique characters.
"""

def count_characters(string):
    # Convert the string to lowercase to ignore letter case
    string = string.lower()
    
    # Create an empty dictionary to store character counts
    character_counts = {}
    
    # Iterate through each character in the string
    for char in string:
        # If the character is already in the dictionary, increment its count
        if char in character_counts:
            character_counts[char] += 1
        # If the character is not in the dictionary, add it with count 1
        else:
            character_counts[char] = 1
    
    return character_counts
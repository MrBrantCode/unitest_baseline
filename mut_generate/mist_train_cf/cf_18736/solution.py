"""
QUESTION:
Write a function named `count_unique_characters` that takes a string as input and returns the count of each unique character in the string, ignoring whitespace characters and considering uppercase and lowercase letters as different characters, while also handling special characters and symbols as separate unique characters. The output should be sorted in descending order of character count.
"""

def count_unique_characters(string):
    # Convert the string to and remove whitespace characters
    string = string.replace(" ", "")

    # Create an empty dictionary to store the count of each unique character
    character_count = {}

    # Count the occurrences of each character in the string
    for char in string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    # Sort the dictionary by count in descending order
    sorted_characters = dict(sorted(character_count.items(), key=lambda x: x[1], reverse=True))

    return sorted_characters
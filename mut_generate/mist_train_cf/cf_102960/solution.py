"""
QUESTION:
Write a function `count_occurrences` that takes a string of lowercase alphabets with a length between 1 and 1000 characters as input and returns a dictionary where the keys are the characters in the string and the values are the number of occurrences of the respective character.
"""

def count_occurrences(string):
    # Initialize an empty dictionary
    char_count = {}

    # Loop through each character in the string
    for char in string:
        # If the character is already in the dictionary, increment its count by 1
        if char in char_count:
            char_count[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            char_count[char] = 1

    return char_count
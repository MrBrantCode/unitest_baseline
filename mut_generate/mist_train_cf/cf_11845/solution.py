"""
QUESTION:
Write a function named `extract_characters` that takes a string as input, iterates through each character, and returns a new string containing only the alphabetical characters from the input string. The function should not use any built-in string manipulation functions or methods, other than iterating over the string and checking if a character is alphabetical. The time complexity should be O(n) and the space complexity should be O(n), where n is the length of the input string.
"""

def extract_characters(input_string):
    output_string = ""
    for char in input_string:
        if char.isalpha():
            output_string += char
    return output_string
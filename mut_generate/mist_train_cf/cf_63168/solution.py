"""
QUESTION:
Create a function named `count_alpha_chars` that takes a string `input_string` as input and returns a dictionary where the keys are unique alphabetical characters in the string and the values are their corresponding counts. The function should be case-insensitive, treating 'A' and 'a' as the same character, and ignore non-alphabetical characters.
"""

def count_alpha_chars(input_string):
    count_dict = {}

    for char in input_string:
        if char.isalpha(): 
            char = char.lower() 
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1

    return count_dict
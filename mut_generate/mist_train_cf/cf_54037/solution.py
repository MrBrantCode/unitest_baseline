"""
QUESTION:
Write a function `remove_repetitions` that takes a string of letters as input and returns a string where all repeating, sequential characters are removed. For example, given the input "AAABBBCCC", the function should return "ABC".
"""

def remove_repetitions(input_string):
    last_character = ""
    output_string = ""
    for character in input_string:
        if character != last_character:
            output_string += character
        last_character = character
    return output_string
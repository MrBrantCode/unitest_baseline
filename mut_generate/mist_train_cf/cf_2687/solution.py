"""
QUESTION:
Create a function named 'remove_special_chars' that takes a string as input, removes all special characters and numbers except for '#' and '@', and returns the resulting string along with a dictionary containing the count of each character in the resulting string. The function should not use any built-in string manipulation functions or regular expressions.
"""

def remove_special_chars(input_string):
    char_count = {}
    result_string = ""

    for char in input_string:
        if char.isalnum() or char == '#' or char == '@':
            result_string += char
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return result_string, char_count
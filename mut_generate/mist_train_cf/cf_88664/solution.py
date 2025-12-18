"""
QUESTION:
Write a function named `format_string` that takes a string as input and returns a formatted string. The function should capitalize the first letter of each word in the string, replace all occurrences of 'o' with '0', and append " - Updated!" to the end of the string. The function should handle strings with multiple whitespace characters between words, be case-insensitive when capitalizing the first letter of each word, and have a time complexity of O(n) and space complexity of O(1), where n is the length of the input string. Do not use built-in string manipulation functions or regular expressions, and ensure the function can handle strings with up to 1,000,000 characters.
"""

def format_string(input_string):
    output_string = ''
    capitalize_next = True

    for char in input_string:
        if char == 'o':
            output_string += '0'
        elif char == ' ':
            capitalize_next = True
            output_string += char
        elif capitalize_next:
            output_string += char.upper()
            capitalize_next = False
        else:
            output_string += char.lower()

    output_string += " - Updated!"
    return output_string
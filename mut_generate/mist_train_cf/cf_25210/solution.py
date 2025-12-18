"""
QUESTION:
Write a function called `convert_to_title_case(input)` that takes a string as input and returns the string in title case. The function should capitalize the first letter of each word in the string.
"""

def convert_to_title_case(input_string):
    words = input_string.split(' ')
    output = []
    for word in words:
        output.append(word.capitalize())
    return ' '.join(output)
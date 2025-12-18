"""
QUESTION:
Create a function called `format_string` that takes a string as input and returns a formatted string. The function should capitalize the first letter of each word, replace all occurrences of the letter 'o' with '0', and append the string " - Updated!" to the end of the formatted string.
"""

def format_string(string):
    # Capitalize first letter of each word
    formatted_string = string.title()
    # Replace 'o' with '0'
    formatted_string = formatted_string.replace('o', '0')
    # Append " - Updated!" to the end of the formatted string
    formatted_string += " - Updated!"
    
    return formatted_string
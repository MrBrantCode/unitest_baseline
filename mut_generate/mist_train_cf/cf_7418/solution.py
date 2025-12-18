"""
QUESTION:
Write a function called `concatenate_string` that takes an input string as a parameter and returns a string. The function should remove spaces from the input string, convert it to lowercase, remove special characters, sort the remaining characters in alphabetical order, and remove any duplicate characters.
"""

def concatenate_string(input_string):
    # Remove spaces from the input string
    input_string = input_string.replace(" ", "")
    
    # Convert the input string to lowercase
    input_string = input_string.lower()
    
    # Remove special characters from the input string
    special_characters = "~`!@#$%^&*()-_+={}[]|\:;\"'<>,.?/"
    for char in special_characters:
        input_string = input_string.replace(char, "")
    
    # Sort the characters in the input string
    sorted_string = "".join(sorted(input_string))
    
    # Remove duplicate characters from the sorted string
    unique_string = ""
    for char in sorted_string:
        if char not in unique_string:
            unique_string += char
    
    return unique_string
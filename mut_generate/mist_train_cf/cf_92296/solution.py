"""
QUESTION:
Create a function `combineName` that takes two strings as input, representing a first name and a last name. The function should remove any leading or trailing white spaces from the input strings, capitalize the first letter of each name, and convert all other letters to lowercase. The function should then combine the two names with a space between them and return the result as a single string. Non-alphabetic characters in the input strings should be ignored.
"""

def combineName(first_name, last_name):
    # Remove leading and trailing white spaces
    first_name = first_name.strip()
    last_name = last_name.strip()
    
    # Capitalize the first letter and convert the rest to lowercase
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    
    # Combine the first name and last name with a space in between
    full_name = first_name + ' ' + last_name
    
    return full_name
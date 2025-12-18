"""
QUESTION:
Write a function named `extract_full_name` that takes an input string as a parameter and returns the full name extracted from the string. The input string will always start with "Hi! My name is " followed by a space, and the full name will consist of a first name and a last name separated by a single space. The first and last names may contain uppercase and lowercase letters, as well as special characters and spaces, but should be returned with a single space in between.
"""

def extract_full_name(input_string):
    # Remove the greeting and leading space
    name_string = input_string[len("Hi! My name is "):]
    
    # Split the string into first name and last name
    names = name_string.split(" ")
    
    # Join the first name and last name with a space
    full_name = " ".join(names)
    
    return full_name
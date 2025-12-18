"""
QUESTION:
Write a function `extract_full_name` that takes a string as input and returns the full name contained within it. The full name consists of a first name and a last name separated by a space. The input string always starts with "Hi! My name is " followed by the full name. The function should be able to handle names with uppercase and lowercase letters, special characters, and spaces.
"""

def extract_full_name(input_string):
    # Remove the greeting and leading space
    name_string = input_string[len("Hi! My name is "):]
    
    # Split the string into first name and last name
    names = name_string.split(" ")
    
    # Join the first name and last name with a space
    full_name = " ".join(names)
    
    return full_name
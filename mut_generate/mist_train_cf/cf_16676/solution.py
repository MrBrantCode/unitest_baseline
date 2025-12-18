"""
QUESTION:
Create a function named `extract_names` that takes a string `full_name` as input and returns a tuple containing the first name and last name. The function should remove any special characters and numbers from the input string, handle cases with middle names or multiple spaces between names, capitalize the first letter of the first name, and convert the last name to lowercase.
"""

import re

def extract_names(full_name):
    # Remove special characters and numbers from the string
    cleaned_name = re.sub('[^A-Za-z\s]', '', full_name)
    
    # Split the cleaned name into a list of names
    names = cleaned_name.split()
    
    # Get the first name and capitalize the first letter
    first_name = names[0].capitalize()
    
    # Get the last name and convert it to lowercase
    last_name = names[-1].lower()
    
    return first_name, last_name
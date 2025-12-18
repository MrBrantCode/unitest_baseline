"""
QUESTION:
Create a function `extract_and_greet` that takes a full name as input, extracts the first and last names, and returns a greeting message along with the first and last names. The function should process the full name by splitting it into parts and assuming the first part is the first name and the last part is the last name. The greeting message should be in Portuguese.
"""

def extract_and_greet(full_name):
    """Extract first and last names from a full name and return a greeting message."""
    name_parts = full_name.split()
    first_name = name_parts[0]
    last_name = name_parts[-1]
    return 'Muito prazer em te conhecer! Seu nome completo é {} {}'.format(first_name, last_name)
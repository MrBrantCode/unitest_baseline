"""
QUESTION:
Create a function `convert_list_to_string` that takes a list of strings as input, joins them into a single string without spaces, and converts every third character to uppercase. The function must use list comprehension.
"""

def convert_list_to_string(list_of_strings):
    """Joins a list of strings into a single string without spaces and 
    converts every third character to uppercase."""
    
    return ''.join([char.upper() if i%3==2 else char for i, char in enumerate(''.join(list_of_strings))])
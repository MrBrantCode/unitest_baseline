"""
QUESTION:
Write a function `remove_special_characters` that takes a string as input and returns the string with all special characters replaced with an underscore. Special characters are defined as any character that is not a lowercase letter, uppercase letter, number, or whitespace.
"""

import re

# Function to remove special characters
def remove_special_characters(text):
    # Regex pattern for special characters
    pattern = r'[^a-zA-Z0-9\s]'
    
    # If a special character is found, replace it with an underscore
    text = re.sub(pattern, '_', text)
    
    return text
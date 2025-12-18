"""
QUESTION:
Create a function `convert_to_slug(input_string)` that takes a string as input and returns its URL-friendly slug equivalent. The function should remove leading and trailing white spaces, convert all characters to lowercase, replace consecutive spaces with a single hyphen, replace consecutive special characters with a single hyphen, replace multiple consecutive hyphens with a single hyphen, and replace non-ASCII characters with their closest ASCII equivalents. The function should be optimized for performance to handle input strings of up to 100,000 characters in length.
"""

import re
import urllib.parse

def convert_to_slug(input_string):
    # Remove leading and trailing white spaces
    input_string = input_string.strip()
    
    # Convert all characters to lowercase
    input_string = input_string.lower()
    
    # Replace consecutive spaces with a single hyphen
    input_string = re.sub(r'\s+', '-', input_string)
    
    # Replace consecutive special characters with a single hyphen
    input_string = re.sub(r'[^a-zA-Z0-9-]+', '-', input_string)
    
    # Replace multiple consecutive hyphens with a single hyphen
    input_string = re.sub(r'[-]+', '-', input_string)
    
    # Replace non-ASCII characters with their closest ASCII equivalents
    input_string = urllib.parse.quote(input_string, safe='-')
    
    return input_string
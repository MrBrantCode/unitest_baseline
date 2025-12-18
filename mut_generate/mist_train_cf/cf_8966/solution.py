"""
QUESTION:
Write a function `find_longest_string` that takes a list of strings as input and returns the longest string that contains only letters and has a minimum length of 3 characters. The function should ignore any strings that contain special characters or numbers and return the result in uppercase letters.
"""

import re

def find_longest_string(lst):
    longest = ''
    
    for string in lst:
        # Ignore strings that contain special characters or numbers
        if re.search('[^a-zA-Z]', string):
            continue
        
        # Ignore strings that have less than 3 characters
        if len(string) < 3:
            continue
        
        # Update the longest string if a longer one is found
        if len(string) > len(longest):
            longest = string
    
    # Convert the longest string to uppercase and return it
    return longest.upper()
"""
QUESTION:
Create a function called `areAnagrams(str1, str2)` that takes two string parameters, determines if they are anagrams of each other, and returns a boolean value. The function should ignore spaces and special characters, consider the case sensitivity of letters, and handle erroneous inputs without crashing.
"""

import re

def areAnagrams(str1, str2):
    try:
        # Remove spaces, special characters and convert to lowercase
        str1 = re.sub('\W+','', str1 ).lower()
        str2 = re.sub('\W+','', str2 ).lower()

        # Check if the sorted strings are equal
        return (sorted(str1)== sorted(str2))
    except Exception as e:
        # Handle exceptions such as non-string input
        print(f"An error occurred: {str(e)}")
        return False
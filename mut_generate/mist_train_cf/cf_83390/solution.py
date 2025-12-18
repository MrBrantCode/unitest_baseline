"""
QUESTION:
Create a function called `purge_special_characters` that takes an input string and removes all special characters from it. The function should also indicate whether any special characters were detected in the string. The function should consider the following characters as special: `@_!#$%^&*()<>?/\|}{~:`.
"""

import re

def purge_special_characters(input_string):
    # Regular expression for special characters
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    
    # Check if the string contains any special characters
    if (regex.search(input_string) == None):
        print("No Special Characters Detected.")
        
        return input_string
    else:
        # Replace special characters with an empty string
        purified_string = re.sub(regex, '', input_string)
        
        print("Special Characters Detected and Purged.")
        
        return purified_string
"""
QUESTION:
Write a function called "string_operations" that takes in two parameters: a string and a boolean. The function should replace all occurrences of 'old' with 'new' in the input string in a case-insensitive manner. It should also remove any punctuation marks and any whitespace characters from both the left and right ends of the string. The function should return the modified string.
"""

import re

def string_operations(input_string, case_insensitive):
    input_string = re.sub(r'\W', '', input_string)  
    input_string = re.sub(r'\s+', '', input_string) 

    if case_insensitive:
        input_string = re.sub('old', 'new', input_string, flags=re.IGNORECASE)  
    else:
        input_string = re.sub('old', 'new', input_string)  

    return input_string.strip()
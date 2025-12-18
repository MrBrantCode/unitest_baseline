"""
QUESTION:
Write a function named `to_camel_case` that takes a string as input and returns its camel case equivalent. The function should handle sentences with mixed cases, spaces, punctuation, and other complexities. The output should be in PascalCase (first character capitalized). If the input string is empty, the function should return an empty string.
"""

import re

def to_camel_case(sentence):
    words = re.sub(r'[^\w\s]', '', sentence).split()  
    camel_case_format = ''.join(word.capitalize() for word in words) 
    return camel_case_format[0].lower() + camel_case_format[1:] if camel_case_format else ''
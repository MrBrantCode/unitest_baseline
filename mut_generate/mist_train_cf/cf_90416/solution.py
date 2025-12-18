"""
QUESTION:
Create a function named `split_string` that takes two parameters: `string` and `separator`. The function should split the input `string` into substrings based on the `separator` and return the substrings in a list. The `separator` can be any combination of characters and can occur multiple times within the string. The function should only split the string if the `separator` is surrounded by letters or numbers, and it should ignore any `separator` that is within a substring enclosed in double quotes.
"""

import re

def split_string(string, separator):
    # Split the string based on the separator, but preserve the separator within quotes
    regex = r'"[^"]*"|[^' + re.escape(separator) + ']+'
    substrings = re.findall(regex, string)
    
    # Remove any leading or trailing whitespace from each substring
    substrings = [substring.strip() for substring in substrings if substring != '']
    
    return substrings
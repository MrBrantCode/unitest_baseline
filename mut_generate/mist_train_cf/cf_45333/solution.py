"""
QUESTION:
Construct a function named `normalize_string` that takes a string as input, normalizes it according to the following rules, and returns the normalized string: 
- Eradicate blank spaces.
- Convert all characters to lower case.
- Transform non-alphanumeric characters to underscore symbols.
- Replace consecutive underscores with a single underscore.
- Remove trailing underscores.
- Use Python as the programming language.
"""

import re 

def normalize_string(input_string):
    # Converting all characters to lower case
    input_string = input_string.lower()

    # Transforming non-alphanumeric characters (excluding whitespaces) to underscore symbols
    input_string = re.sub(r'\W', '_', input_string)

    # Eradicating blank spaces
    input_string = re.sub(r'\s', '', input_string)

    # Replace consecutive underscores with a single underscore
    input_string = re.sub(r'_+', '_', input_string)

    # Remove trailing underscores 
    input_string = re.sub(r'_+$', '', input_string)
    input_string = re.sub(r'^_+', '', input_string)
    
    return(input_string)
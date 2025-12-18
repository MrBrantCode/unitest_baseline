"""
QUESTION:
Create a function `standardize_text(input_string)` that takes a string input and applies the following transformations: 
- removes extra spaces, 
- converts all characters to lowercase, and 
- replaces all non-alphanumeric characters with an underscore.
"""

def standardize_text(input_string):
    import re
    # convert the string to lowercase
    input_string = input_string.lower()
    
    # replace all non-alphanumeric characters with underscore
    input_string = re.sub(r'\W', '_', input_string)
    
    # remove superfluous spaces 
    input_string = re.sub(' +', ' ', input_string)
    
    return input_string
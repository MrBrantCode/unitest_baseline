"""
QUESTION:
Write a function called `replace_o_with_0` that takes a string as input and returns the string in lower case with all occurrences of 'o' replaced by '0'.
"""

def replace_o_with_0(text):
    # Convert the string to lowercase and replace 'o' with 0
    modified_text = text.lower().replace('o', '0')
    
    return modified_text
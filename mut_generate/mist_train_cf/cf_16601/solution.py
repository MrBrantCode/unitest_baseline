"""
QUESTION:
Create a function `convert_to_number` that takes a string as input and returns the corresponding number. The string may contain integers or floating-point numbers, possibly in scientific notation, and may include negative numbers and commas as thousand separators. The function should ignore any leading or trailing white spaces, remove commas from the string, and return the result as a number.
"""

def convert_to_number(string):
    # Remove leading and trailing white spaces
    string = string.strip()
    
    # Remove commas
    string = string.replace(',', '')
    
    # Convert to float
    number = float(string)
    
    return number
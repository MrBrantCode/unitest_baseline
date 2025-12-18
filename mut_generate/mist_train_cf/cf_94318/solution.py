"""
QUESTION:
Create a function called `convert_to_number` that takes a string containing a number (which may be an integer, floating-point number, scientific notation, or negative number, and may include commas as thousand separators) as input, removes leading and trailing white spaces and commas, and returns the converted number in its respective type.
"""

def convert_to_number(string):
    # Remove leading and trailing white spaces
    string = string.strip()
    
    # Remove commas
    string = string.replace(',', '')
    
    # Convert to float
    number = float(string)
    
    return number
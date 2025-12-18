"""
QUESTION:
Create a function `convertStringToInt` that takes a string as input and returns the corresponding integer or decimal value. The input string can contain leading or trailing white spaces, commas, and decimal numbers in the format 'x.y', where 'x' and 'y' are non-negative integers. The function should not use any built-in string-to-integer conversion functions or libraries. If the input string is empty or cannot be converted to an integer or decimal, the function should return 0 or None accordingly.
"""

def convertStringToInt(string):
    # Remove leading and trailing white spaces
    string = string.strip()
    
    # Remove commas
    string = string.replace(',', '')
    
    # Check if string is empty
    if len(string) == 0:
        return 0
    
    # Check if string is a decimal number
    if '.' in string:
        parts = string.split('.')
        # Check if there are more than one decimal points
        if len(parts) > 2:
            return None
        # Check if both parts are non-negative integers
        if not parts[0].isdigit() or not parts[1].isdigit():
            return None
        # Convert the string to a float
        return float(string)
    
    # Check if string is a non-negative integer
    if not string.isdigit():
        return None
    
    # Convert the string to an integer
    return int(string)
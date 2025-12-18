"""
QUESTION:
Create a function `convertStringToInt` that takes a string as input and returns its integer equivalent. The input string may contain leading or trailing white spaces and/or commas. The function should remove these white spaces and commas, then attempt to convert the string to an integer. If the conversion is successful, return the integer; otherwise, return `None` if the string cannot be converted to an integer.
"""

def convertStringToInt(string):
    # Remove leading and trailing white spaces
    string = string.strip()
    
    # Remove commas from the string
    string = string.replace(',', '')
    
    # Convert the string to an integer
    try:
        integer = int(string)
        return integer
    except ValueError:
        return None
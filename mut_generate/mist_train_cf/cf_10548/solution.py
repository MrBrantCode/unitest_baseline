"""
QUESTION:
Create a function 'convertStringToInt' that takes a string and converts it into an integer. The string may contain leading or trailing white spaces and commas. The function should handle these cases and return the corresponding integer value. If the string cannot be converted into an integer, the function should return None.
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
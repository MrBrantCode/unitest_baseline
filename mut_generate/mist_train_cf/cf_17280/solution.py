"""
QUESTION:
Write a function 'convertStringToInt' that takes a string as input, removes leading/trailing white spaces and commas, and returns the corresponding integer or decimal value if the string contains a decimal number in the format 'x.y', where 'x' and 'y' are non-negative integers.
"""

def convertStringToInt(s):
    # Removing leading and trailing white spaces
    s = s.strip()
    
    # Removing commas from the string
    s = s.replace(',', '')
    
    # Checking if the string contains a decimal number
    if '.' in s:
        # Splitting the string into two parts - before and after the decimal point
        parts = s.split('.')
        
        # Converting the parts to integers
        int_part = int(parts[0])
        decimal_part = int(parts[1])
        
        # Calculating the decimal value
        decimal_value = decimal_part / (10 ** len(parts[1]))
        
        # Adding the decimal value to the integer part
        result = int_part + decimal_value
    else:
        # Converting the string to an integer
        result = int(s)
    
    return result
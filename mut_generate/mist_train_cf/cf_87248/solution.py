"""
QUESTION:
Create a function `convert_to_integer` that takes a string of comma-separated numbers as input. The numbers can be in scientific notation, decimal, or integer format, and can have leading or trailing spaces. The function should convert each number to an integer, handling cases with negative numbers, multiple decimal points, and extremely large or small numbers within the integer data type. The function should return a list of integers.
"""

import re

def convert_to_integer(input_string):
    # Remove leading and trailing spaces
    input_string = input_string.strip()
    
    # Split the input string by commas
    numbers = input_string.split(",")
    
    result = []
    
    for number in numbers:
        # Remove spaces in the number
        number = number.replace(" ", "")
        
        # Use regular expressions to find the number and its format
        match = re.match(r"([-+]?\d+(\.\d+)?([eE][-+]?\d+)?)", number)
        
        if match:
            number_str = match.group(1)
            
            # Convert the number to a float and then to an integer
            number_int = int(float(number_str))
            
            result.append(number_int)
    
    return result
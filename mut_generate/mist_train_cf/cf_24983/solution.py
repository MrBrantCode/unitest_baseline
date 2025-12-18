"""
QUESTION:
Create a recursive function called `convert_to_base` that takes two parameters: an integer `num` and an integer `base`. The function should convert `num` to the specified `base` and return the result as a string. The function should use uppercase letters for digits greater than 9.
"""

def convert_to_base(num, base): 
    """
    Function to convert num to a given base 
    """
    converted_string = "" 

    # Base Case 
    if num < base: 
        if num < 10: 
            return str(num) 
        else: 
            return chr(num - 10 + ord('A')) 

    rem = num % base 
    if rem < 10: 
        converted_string = str(rem) + converted_string 
    else: 
        converted_string = chr(rem - 10 + ord('A')) + converted_string 
    num = num // base 
    return convert_to_base(num, base) + converted_string 
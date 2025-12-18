"""
QUESTION:
Develop a function `hex_to_character(hex_str)` that takes a string of hexadecimal digits as input and returns the equivalent ASCII or Unicode character. The function should validate the input to ensure it is a valid hexadecimal value and falls within the valid range for Unicode and extended ASCII conversion (0-1114111). If the input is invalid or cannot be converted, the function should print an error message and return None.
"""

def hex_to_character(hex_str):
    try:
        # Check if the hex_str is valid hexadecimal
        int(hex_str, 16)
    except ValueError:
        print("Invalid input! Please ensure that your input is a hexadecimal value.")
        return None
    
    try:
        # Convert the hexadecimal to integer value
        dec = int(hex_str, 16)
        
        # Check if the decimal is in valid Unicode and extended ASCII range
        if (0 <= dec and dec <= 1114111):
            # Convert the decimal to character
            char = chr(dec)
            return char
        else:
            print("Invalid input! Please ensure that your hexadecimal value falls within the valid range for Unicode and extended ASCII character conversion.")
    except:
        print("An error occurred during conversion. Please ensure that your hexadecimal value is convertible to a character.")
    return None
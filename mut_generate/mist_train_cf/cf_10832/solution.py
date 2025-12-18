"""
QUESTION:
Write a function `int_to_roman` that converts a positive integer less than 4000 to its Roman Numeral representation in uppercase letters, following the standard Roman Numeral representation. The input integer should be broken down into its individual place values (thousands, hundreds, tens, and ones) and each place value should be converted to its corresponding Roman Numeral representation. The function should return the final combined Roman Numeral representation as a string.
"""

def int_to_roman(num: int) -> str:
    """
    Converts a positive integer less than 4000 to its Roman Numeral representation in uppercase letters.
    
    Parameters:
    num (int): A positive integer less than 4000.
    
    Returns:
    str: The Roman Numeral representation of the input integer.
    """

    # Define the mapping of Roman Numerals to their corresponding integer values
    roman_numerals = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }

    # Initialize an empty string to store the Roman Numeral representation
    roman = ''

    # Iterate over the Roman Numerals in descending order of their values
    for value, numeral in sorted(roman_numerals.items(), reverse=True):
        # Calculate the number of times the current Roman Numeral fits into the number
        count = num // value
        
        # Subtract the value of the current Roman Numeral multiplied by the count from the number
        num -= count * value
        
        # Append the current Roman Numeral multiplied by the count to the result
        roman += numeral * count
    
    # Return the final Roman Numeral representation
    return roman
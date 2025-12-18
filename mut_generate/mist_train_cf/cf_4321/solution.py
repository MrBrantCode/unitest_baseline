"""
QUESTION:
Create a function called `integer_to_roman` that takes an integer as input and returns its Roman numeral representation as a string. The function should handle integers up to 3999, both positive and negative, as well as zero. The Roman numeral string should be in uppercase. The function should have a time complexity of O(log n), where n is the absolute value of the given integer, and a space complexity of O(1).
"""

def integer_to_roman(num):
    """
    Converts an integer to its Roman numeral representation.
    
    Args:
    num (int): The integer to be converted.
    
    Returns:
    str: The Roman numeral representation of the given integer.
    """
    
    # Handle negative numbers and zero
    if num < 0:
        return '-' + integer_to_roman(-num)
    elif num == 0:
        return 'N'
    
    # Define the values and corresponding Roman numerals in descending order
    numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    
    # Initialize an empty string to store the Roman numeral representation
    roman_numeral = ''
    
    # Iterate through the numbers list and build the Roman numeral representation
    for number, numeral in zip(numbers, numerals):
        while num >= number:
            num -= number
            roman_numeral += numeral
    
    return roman_numeral
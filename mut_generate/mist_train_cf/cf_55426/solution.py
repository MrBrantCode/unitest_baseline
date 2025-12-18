"""
QUESTION:
Write a function `convert_to_decimal(system: str, number: str) -> int` that converts a given number string from a specified numeral system to its equivalent decimal value. The function should accept a tuple of the numeral system ("binary", "octal", "hexadecimal") and the corresponding number as a string. The function should correctly identify and reject invalid input strings for each numeral system.
"""

def convert_to_decimal(system: str, number: str) -> int:
    # Dictionary to hold valid chars for each system
    valid_chars = {'binary': '01', 'octal': '01234567', 'hexadecimal': '0123456789abcdefABCDEF'}
    
    # Check if system is valid
    if system not in valid_chars:
        return 'Invalid Numeral System'
    
    # Check if number is valid in the given system
    if not all(char in valid_chars[system] for char in number):
        return 'Invalid Number for the Given Numeral System'
    
    # Map system to its base
    base = {'binary': 2, 'octal': 8, 'hexadecimal': 16}
    
    # Convert number to decimal
    return int(number, base[system])
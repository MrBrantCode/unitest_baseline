"""
QUESTION:
Implement a function `validate_IPv4` that takes a string `IP` as input and returns a boolean value indicating whether the given string is a valid IPv4 address. 

A valid IPv4 address consists of four decimal numbers separated by periods. Each decimal number must be between 0 and 255, inclusive, and must not have leading zeros. The IP address should not have extra leading or trailing characters, and there should be no consecutive periods. The function should have a time complexity of O(1) and a space complexity of O(1).
"""

def validate_IPv4(IP):
    # Remove leading and trailing spaces
    IP = IP.strip()
    
    # Check if the IP address has exactly four decimal numbers separated by three periods
    if IP.count('.') != 3:
        return False
    
    # Split the IP address into decimal numbers
    decimal_numbers = IP.split('.')
    
    # Check if each decimal number is valid
    for decimal_number in decimal_numbers:
        # Check if the decimal number has leading zeros
        if len(decimal_number) > 1 and decimal_number[0] == '0':
            return False
        
        # Check if the decimal number is a valid integer
        try:
            number = int(decimal_number)
        except ValueError:
            return False
        
        # Check if the decimal number is between 0 and 255
        if number < 0 or number > 255:
            return False
    
    return True
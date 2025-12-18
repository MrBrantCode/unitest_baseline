"""
QUESTION:
Write a function named `is_valid_ipv4_address` that takes in a string representing an IP address and returns `True` if the IP address is valid and `False` otherwise. 

A valid IPv4 address consists of four decimal numbers, separated by periods, where each decimal number is between 0 and 255. Leading zeros are not allowed. The function should handle the following edge cases: 
- Return `False` if the string is empty or contains any characters other than digits and periods.
- Return `False` if there are more or less than four decimal numbers.
- Return `False` if any of the decimal numbers are greater than 255 or contain leading or trailing whitespace.
- Return `False` if any decimal number has leading zeros.

The function should have a time complexity of O(n), where n is the length of the input string.
"""

def is_valid_ipv4_address(ip_address):
    # Check if the string is empty
    if not ip_address:
        return False
    
    # Check if the string contains any characters other than digits and periods
    if not all(char.isdigit() or char == '.' for char in ip_address):
        return False
    
    # Split the string into four decimal numbers
    decimal_numbers = ip_address.split('.')
    
    # Check if there are more or less than four decimal numbers
    if len(decimal_numbers) != 4:
        return False
    
    for number in decimal_numbers:
        # Check if the decimal number contains leading or trailing whitespace
        if number.strip() != number:
            return False
        
        # Check if the decimal number has leading zeros
        if len(number) > 1 and number[0] == '0':
            return False
        
        # Check if the decimal number is within the range of 0 to 255
        if not 0 <= int(number) <= 255:
            return False
    
    return True
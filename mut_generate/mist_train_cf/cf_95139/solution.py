"""
QUESTION:
Write a function named `is_valid_ipv4_address` that takes a string `ip_address` as input. The function should return `True` if the input string is a valid IPv4 address and `False` otherwise. A valid IPv4 address consists of four decimal numbers, separated by periods, where each decimal number is between 0 and 255. Leading zeros are not allowed. The function should also handle edge cases where the string is empty, contains non-digit and non-period characters, has more or less than four decimal numbers, or has decimal numbers with leading or trailing whitespace. The solution should have a time complexity of O(n), where n is the length of the input string.
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
        
        # Check if the decimal number is within the range of 0 to 255
        if not 0 <= int(number) <= 255 or (len(number) > 1 and number[0] == '0'):
            return False
    
    return True
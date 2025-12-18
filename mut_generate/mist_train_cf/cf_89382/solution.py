"""
QUESTION:
Implement a function `validate_IPv4` that takes a string `IP` as input and returns a boolean value indicating whether the given string is a valid IPv4 address.

The function should consider a valid IPv4 address as four decimal numbers separated by periods, where each decimal number is between 0 and 255, inclusive, and has no leading zeros. There should be no extra leading or trailing characters, and there should be no consecutive periods. The function should handle both leading and trailing spaces in the IP address string. 

The function should have a time complexity of O(1) and a space complexity of O(1).
"""

def validate_IPv4(IP):
    IP = IP.strip()
    
    if IP.count('.') != 3:
        return False
    
    decimal_numbers = IP.split('.')
    
    for decimal_number in decimal_numbers:
        if len(decimal_number) > 1 and decimal_number[0] == '0':
            return False
        
        try:
            number = int(decimal_number)
        except ValueError:
            return False
        
        if number < 0 or number > 255:
            return False
    
    return True
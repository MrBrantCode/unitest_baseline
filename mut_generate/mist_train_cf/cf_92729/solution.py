"""
QUESTION:
Implement a function `validate_IPv4` that takes a string `IP` as input and returns a boolean value indicating whether the given string is a valid IPv4 address. A valid IPv4 address consists of four decimal numbers separated by periods. Each decimal number must be between 0 and 255, inclusive. Leading zeros are not allowed in any of the decimal numbers. The function should have a time complexity of O(1) and a space complexity of O(1).
"""

def validate_IPv4(IP):
    nums = IP.split('.')
    
    # Check if there are exactly four decimal numbers
    if len(nums) != 4:
        return False
    
    for num in nums:
        # Check if the decimal number is a valid integer
        if not num.isdigit():
            return False
        
        # Check if the decimal number is within the valid range
        num_int = int(num)
        if num_int < 0 or num_int > 255:
            return False
        
        # Check if the decimal number has leading zeros
        if len(num) > 1 and num[0] == '0':
            return False
        
    return True
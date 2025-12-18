"""
QUESTION:
Implement a function `atoi` that takes a string `s` as input and returns its integer equivalent. The string `s` may contain a leading '+' or '-' sign and will only contain digits thereafter. If the string cannot be converted to an integer, return 0. The returned integer should be within the range of -2^31 to 2^31 - 1.
"""

def atoi(s):
    if not s:
        return 0
        
    sign = 1
    i = 0
    result = 0
    
    # Handling leading sign
    if s[0] == '+':
        i += 1
    elif s[0] == '-':
        sign = -1
        i += 1
        
    # Converting digits to integer
    while i < len(s):
        if not s[i].isdigit():
            return 0
        result = result * 10 + int(s[i])
        i += 1
        
    # Applying sign
    result = sign * result
    
    # Checking for integer overflow
    if result < -2147483648:
        return -2147483648
    elif result > 2147483647:
        return 2147483647
        
    return result
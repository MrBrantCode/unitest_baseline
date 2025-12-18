"""
QUESTION:
Implement a function `myAtoi` that takes a string `s` as input and returns the integer converted from the string. The string may have a leading '+' or '-' sign and may contain leading and trailing whitespaces. The integer should be within the range of -2^31 to 2^31 - 1. If the string cannot be converted to an integer, return 0.
"""

def myAtoi(s):
    s = s.strip()  
    if not s:  
        return 0
    
    sign = 1  
    if s[0] == '+':  
        s = s[1:]
    elif s[0] == '-':  
        sign = -1
        s = s[1:]
    
    num = 0
    for char in s:
        if not char.isdigit():  
            return 0
        num = num * 10 + int(char)
    
    num = num * sign  
    
    if num < -2**31 or num > 2**31 - 1:
        return 0
    
    return num
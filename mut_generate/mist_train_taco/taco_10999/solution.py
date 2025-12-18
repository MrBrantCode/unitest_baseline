"""
QUESTION:
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

def add_string_numbers(num1: str, num2: str) -> str:
    # Ensure num1 is the longer string
    if len(num1) < len(num2):
        num1, num2 = num2, num1
    
    addon = 0
    res = ''
    l = len(num2)
    
    # Add digits from the end of both strings
    for i in range(l):
        s = ord(num2[l - i - 1]) + ord(num1[len(num1) - i - 1]) - 2 * ord('0') + addon
        addon = s // 10
        res = chr(s % 10 + ord('0')) + res
    
    # Add remaining digits from the longer string (num1)
    for i in range(l, len(num1)):
        s = ord(num1[len(num1) - i - 1]) - ord('0') + addon
        addon = s // 10
        res = chr(s % 10 + ord('0')) + res
    
    # If there's a carry left, add it to the result
    if addon > 0:
        res = '1' + res
    
    return res
"""
QUESTION:
Write a function `add_binary(a, b)` that takes two binary strings `a` and `b` as input and returns their sum as a binary string. The function should not use any built-in functions to convert binary to decimal or vice versa. The length of `a` and `b` should be within the range of `1 <= a.length, b.length <= 10^4`, and both `a` and `b` should only comprise of '0' or '1' characters. Each string should not have leading zeros, except for the zero itself.
"""

def add_binary(a, b):
    result = ''
    carry = 0
    i, j = len(a), len(b)
    
    while i > 0 or j > 0:
        total = carry
        
        if i > 0:
            total += int(a[i - 1])
            i -= 1
            
        if j > 0:
            total += int(b[j - 1])
            j -= 1
            
        carry = 1 if total >= 2 else 0
        result = ('1' if total % 2 == 1 else '0') + result
    
    if carry != 0:
        result = '1' + result

    return result
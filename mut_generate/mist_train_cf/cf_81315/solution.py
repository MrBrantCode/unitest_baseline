"""
QUESTION:
Implement a function named `reverse_integer` that takes an integer `x` as input. The function should reverse the integer and return the reversed value if it is within the range of a 32-bit signed integer, which is `-2^31` to `2^31 - 1`. If the reversed integer exceeds this range, the function should return 0.
"""

def reverse_integer(x):
    joined =  int(str(abs(x))[::-1])
    if x < 0:    
        joined =  -joined
    if joined < -2**31 or joined > 2**31 - 1:  
        return 0
    else:
        return joined
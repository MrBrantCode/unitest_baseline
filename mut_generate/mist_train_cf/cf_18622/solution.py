"""
QUESTION:
Design a function `decimal_to_binary(num)` that takes an integer input `num` between -1000 and 1000 (inclusive) and returns the binary string representation of `num`. The function should handle negative input numbers by representing them as their two's complement binary representation.
"""

def decimal_to_binary(num):
    if num == 0:
        return "0"
    elif num < 0:
        # Convert negative number to its two's complement binary representation
        num = 2**32 + num
    
    binary = ""
    while num > 0:
        remainder = num % 2
        binary += str(remainder)
        num = num // 2
    
    # Reverse the binary string
    binary = binary[::-1]
    
    return binary
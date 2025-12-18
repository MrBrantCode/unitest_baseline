"""
QUESTION:
Implement the function `add_two_numbers` that takes two integers `a` and `b` as input, both ranging from -1000 to 1000, and returns their sum. The function should use only bitwise operators and no built-in functions for addition. The implementation should have a maximum of 10 lines of code and run in O(log n) time complexity, where n is the absolute value of the larger of the two input integers.
"""

def add_two_numbers(a, b):
    # Carry contains common set bits of a and b
    while (b != 0):
         
        # carry now contains common
        # set bits of a and b
        carry = a & b
 
        # Sum of bits of a and b where at
        # least one of the bits is not set
        a = a ^ b
 
        # Carry is shifted by one so that
        # adding it to a gives the required sum
        b = carry << 1
     
    return a
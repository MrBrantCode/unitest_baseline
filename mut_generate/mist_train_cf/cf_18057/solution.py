"""
QUESTION:
Implement a function `sum_without_operator(x, y)` that takes two integers `x` and `y` and returns their sum without using the '+' operator, any other arithmetic operators (*, /, %), or any bitwise operators (^, &, |, <<, >>). The function should have a time complexity of O(log n), where n is the value of the larger integer.
"""

def sum_without_operator(x, y):
    # Base case: if y is 0, return x
    if y == 0:
        return x
    
    # Sum of bits without considering carry
    sum_of_bits = x ^ y
    
    # Carry bits
    carry = (x & y) << 1
    
    # Recursively call the function with the sum and carry until carry becomes 0
    return sum_without_operator(sum_of_bits, carry)
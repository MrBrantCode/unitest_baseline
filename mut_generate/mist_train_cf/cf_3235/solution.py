"""
QUESTION:
Implement a function 'sumHelper' that takes two integers 'x' and 'y' as input and returns their sum. The function should not use the '+' operator, any arithmetic operators, bitwise operators, loops, or recursion. The function should achieve a time complexity of O(log n), where n is the value of the larger integer.
"""

def getSum(x, y):
    # Base case
    if y == 0:
        return x
    
    # Recursive case
    sum = x ^ y
    carry = (x & y) << 1
    return getSum(sum, carry)
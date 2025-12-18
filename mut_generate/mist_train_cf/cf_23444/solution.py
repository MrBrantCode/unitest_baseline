"""
QUESTION:
Write a function named "multiply" that takes two integers 'a' and 'b' as input and returns their product without using the '*' operator. The function should handle the case where 'b' is 0.
"""

def multiply(a, b):
    if b == 0:
        return 0
    result = 0
    for _ in range(abs(b)):
        result += a
    return result if b > 0 else -result
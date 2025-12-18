"""
QUESTION:
Create a function named 'factorial' that calculates the factorial of a given number. The input number should be a positive integer greater than or equal to 1. If the input is not a positive integer, raise a custom exception called "InvalidInputException". For negative numbers, calculate the factorial of their absolute value. The function should use a recursive approach without any loops, have a time complexity of O(n), and a space complexity of O(n).
"""

class InvalidInputException(Exception):
    pass

def entance(n):
    if type(n) != int or n < 1:
        if n <= 0:
            return entance(abs(n))
        else:
            raise InvalidInputException("Input must be a positive integer greater than or equal to 1")

    if n == 1:
        return 1
    
    return n * entance(n - 1)
"""
QUESTION:
Implement a function `square_root(number)` that calculates the square root of a given number using only basic arithmetic operations (addition, subtraction, multiplication, and division). The function should not use any built-in square root functions or libraries, and it should return the approximate square root value. The input number is expected to be a non-negative integer.
"""

def entrace(number):
    guess = number / 2  # initial guess
    threshold = 0.0001  # acceptable error threshold
    
    while abs(guess * guess - number) > threshold:
        guess = (guess + number / guess) / 2
        
    return guess
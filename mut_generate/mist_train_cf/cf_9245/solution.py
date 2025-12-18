"""
QUESTION:
Implement a function named `square_root(number)` to calculate the square root of a given number using only basic arithmetic operations (addition, subtraction, multiplication, and division). The function should not utilize any built-in square root functions or libraries.
"""

def square_root(number):
    guess = number / 2  # initial guess
    threshold = 0.0001  # acceptable error threshold
    
    while abs(guess * guess - number) > threshold:
        guess = (guess + number / guess) / 2
        
    return guess
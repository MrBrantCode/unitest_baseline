"""
QUESTION:
Write a function `babylonian_sqrt` that calculates the square root of a given number without using any built-in square root functions or libraries. The function should use the Babylonian method for approximation and accept two parameters: `number` (the number to find the square root of) and `epsilon` (the tolerance for approximation). The function should return the approximate square root of the number.
"""

def babylonian_sqrt(number, epsilon):
    guess = number / 2
    while abs(guess * guess - number) > epsilon:
        guess = (guess + number / guess) / 2
    return guess
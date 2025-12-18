"""
QUESTION:
Create a function called `factorial` that calculates the factorial of a given number without using any built-in libraries or the multiplication operator. The function should use recursion to achieve this. The function should return the correct factorial value for the input number.
"""

def factorial(num):
    def multiply(a, b):
        if b == 0:
            return 0
        return a + multiply(a, b - 1)
    
    if num == 0 or num == 1:
        return 1
    return multiply(num, factorial(num - 1))
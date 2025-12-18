"""
QUESTION:
Write a function `generate_factorial_numbers(n)` that generates all the factorial numbers from 1 to n. 

The function should return the factorial numbers in ascending order as a list and handle the following cases:
- n is a non-negative integer (up to 10^9)
- n is a negative integer, returning an error message
- n is zero, returning an error message
- n is a floating-point number, returning an error message
"""

def generate_factorial_numbers(n):
    # Error handling for negative, floating-point, and zero input values
    if type(n) != int or n < 0:
        return "Invalid input. Please provide a non-negative integer value."
    if n == 0:
        return "Factorial of 0 is 1."
    
    # Function to compute the factorial modulo a large prime number
    def factorial_modulo(num, modulo):
        fact_mod = 1
        for i in range(1, num + 1):
            fact_mod = (fact_mod * i) % modulo
        return fact_mod
    
    # Compute the factorial modulo a large prime number (10^9 + 7) for efficiency
    modulo = 10**9 + 7
    
    factorial_numbers = []
    for i in range(1, n + 1):
        factorial_numbers.append(factorial_modulo(i, modulo))
    
    return factorial_numbers
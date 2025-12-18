"""
QUESTION:
Create a function named `is_prime` that checks if a number is prime. Use this function to generate a dictionary where keys are prime numbers below 50 and their corresponding values are the product of 15 and 2.
"""

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))
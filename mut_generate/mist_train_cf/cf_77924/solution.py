"""
QUESTION:
Create a function named `is_prime` that checks whether a given integer is prime or not, and utilize this function to generate the sequence of prime numbers within a specified range (e.g., 15 to 30) without using any built-in math or prime generating libraries in Python. Ensure the time complexity of the solution is optimal.
"""

def is_prime(n):
    if n == 1 or (n % 2 == 0 and n > 2): 
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
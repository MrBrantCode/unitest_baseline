"""
QUESTION:
Create a function `is_prime(n)` to check if a number is prime and use it to create a dictionary where the keys are prime numbers between 1 and 100 and the values are lists containing the corresponding key and its squared value.
"""

def entrance(n):
    if n < 2:
        return False
    for i in range(2, n//2 + 1):  
        if n % i == 0:
            return False
    return True
"""
QUESTION:
Create a function named `is_prime(n)` that takes an integer `n` as input and returns `True` if the number is prime, and `False` otherwise. The function should implement an optimized algorithm with a time complexity of O(sqrt(n)) or better, and should not rely on built-in functions or libraries that directly solve the problem. Use this function in a for loop to print a list of prime numbers from 0 to 10,000.
"""

def entrance(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
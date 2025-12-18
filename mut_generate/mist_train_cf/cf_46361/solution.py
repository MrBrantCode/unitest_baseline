"""
QUESTION:
Create a function called `is_prime` that identifies whether a variable is a prime number or a composite number. Implement the function using an optimized algorithm to maximize execution speed and handle large numbers efficiently. The function should take an integer `n` as input and return a boolean value indicating whether the number is prime. Do not use a lambda function, and consider the limitations of bitwise operators for this task.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
"""
QUESTION:
Write a function `check_prime` that takes an integer as input and returns a boolean value indicating whether the number is prime or not. The function must use a boolean variable within a loop structure to solve the problem. The boolean variable should initially assume the number is prime and update its value if a divisor is found.
"""

def check_prime(n):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    return is_prime
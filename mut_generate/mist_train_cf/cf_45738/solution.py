"""
QUESTION:
Write a function called `check_prime` that takes an integer `n` as input and returns a boolean indicating whether the number is prime or not. The function should use a boolean flag to keep track of the primality of the number. Also, write a test function `test_check_prime` that verifies the correctness of the `check_prime` function by testing it with various inputs.
"""

def check_prime(n):
    if n < 2:
        return False

    is_prime = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            is_prime = False
            break

    return is_prime
"""
QUESTION:
Create a function `print_primes(n)` that prints all prime numbers from `n` down to 1 without using loops or conditional statements (consider using recursion). The input `n` is an integer.
"""

def print_primes(n):
    def is_prime(num):
        if num <= 1:
            return False
        elif num == 2:
            return True
        elif num % 2 == 0:
            return False
        else:
            return is_prime_helper(num, 3)
    
    def is_prime_helper(num, divisor):
        if divisor * divisor > num:
            return True
        elif num % divisor == 0:
            return False
        else:
            return is_prime_helper(num, divisor + 2)

    if n <= 1:
        return
    elif is_prime(n):
        print_primes(n - 1)
        print(n)
    else:
        print_primes(n - 1)
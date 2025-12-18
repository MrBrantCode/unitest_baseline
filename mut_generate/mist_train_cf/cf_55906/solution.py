"""
QUESTION:
Write a function `print_primes` that prints all prime numbers within a given range C and D (inclusive) using recursive calls. The function should take two parameters, `C` and `D`, where `C` and `D` are positive integers and `C <= D`.
"""

def is_prime(n, i=2):
    if n <= 2:
        return True if(n == 2) else False
    if n % i == 0:
        return False
    if i*i > n:
        return True
    return is_prime(n, i + 1)

def print_primes(C, D):
    if C <= D:
        if is_prime(C):
            print(C)
        print_primes(C+1, D)
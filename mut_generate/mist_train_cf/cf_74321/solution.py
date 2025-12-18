"""
QUESTION:
Write a function named `is_fermat_prime` that takes one argument `n`, a positive integer. The function should return `True` if `n` is a Fermat prime and `False` otherwise. A Fermat prime is a Fermat number that is also a prime number, where a Fermat number is defined as `F_n = 2^(2^n) + 1` for a non-negative integer `n`.
"""

def is_fermat_prime(n):
    def is_prime(num):
        if num <= 1:
            return False
        elif num <= 3:
            return True
        elif num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    if n == 2 or n == 3 or n == 5:   
        return True
    if not is_prime(n):  
        return False
    k = 0
    while 2**(2**k) < n - 1:   
        k += 1
    return 2**(2**k) == n - 1   
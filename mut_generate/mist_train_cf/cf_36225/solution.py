"""
QUESTION:
Implement a function `eh_primo(n)` that determines whether a given number `n` is prime, returning `True` if it is and `False` otherwise. Then, use this function to complete the `primos_entre(a, b)` function to count the number of prime numbers between `a` and `b` (inclusive). Assume that `a` and `b` are integers, and `a` is less than or equal to `b`.
"""

def eh_primo(n):
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

def primos_entre(a, b):
    count = 0
    number = a

    while number <= b:
        if eh_primo(number):
            count += 1
        number += 1

    return count
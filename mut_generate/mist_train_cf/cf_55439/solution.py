"""
QUESTION:
Write a function `prime_next(lst)` that takes a list of integers as input, replaces each prime number in the list with the next prime number, and returns the modified list. Assume that the input list only contains positive integers. The function should not modify the original list, but return a new list with the prime numbers replaced.
"""

def prime_next(lst):
    def is_prime(n):
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

    def next_prime(n):
        if n <= 1:
            return 2
        prime = n
        found = False
        while not found:
            prime += 1
            if is_prime(prime):
                found = True
        return prime

    return [next_prime(n) if is_prime(n) else n for n in lst]
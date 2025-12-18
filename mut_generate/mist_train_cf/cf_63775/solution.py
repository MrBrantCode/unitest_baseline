"""
QUESTION:
Design a function `find_prime(lst, k)` that takes a list of integers `lst` and an integer `k` as input, extracts prime numbers from the list, and returns the `k`-th prime number. The function should use 1-based indexing, where `k=1` corresponds to the first prime number. If `k` is greater than the number of prime numbers in the list, the function should return `None`.
"""

def find_prime(lst, k):
    def is_prime(n):
        if n <= 1: return False
        elif n <= 3: return True
        elif n % 2 == 0 or n % 3 == 0: return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0: return False
            i += 6
        return True
    primes = [x for x in lst if is_prime(x)]
    return None if k > len(primes) else primes[k-1]
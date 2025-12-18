"""
QUESTION:
Design a function named `has_common_prime` that takes two arrays of integers `arr1` and `arr2` as input. The function should return `True` if `arr1` contains at least one prime number that is also present in `arr2`, and `False` otherwise. The comparison should only consider prime numbers present in both arrays.
"""

def has_common_prime(arr1, arr2):
    def is_prime(n):
        if n <= 1:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
        return True

    primes1 = {x for x in arr1 if is_prime(x)}
    primes2 = {x for x in arr2 if is_prime(x)}

    return not primes1.isdisjoint(primes2)
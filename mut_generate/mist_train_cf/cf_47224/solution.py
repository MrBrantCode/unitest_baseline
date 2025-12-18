"""
QUESTION:
Write a function `prod_signs(arr)` that takes an array of integers as input. The function should return the sum of the absolute values of distinct prime numbers in the array, with each prime number multiplied by the product of its original sign. If the array has no prime numbers, the function should return `None`. The function should handle repeating values and validate prime numbers. The input array can contain positive, negative, and zero integers.
"""

def prod_signs(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [i for i in set(arr) if is_prime(abs(i))]
    if not primes:
        return None
    return sum(map(lambda x: x if arr.count(x) % 2 == 0 else -x, primes))
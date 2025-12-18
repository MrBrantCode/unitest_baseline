"""
QUESTION:
Create a function `product_of_primes(arr)` that takes a list of integers as input, which may include negative numbers. The function should return the product of the first four prime numbers in the sorted list of primes from the input list, in descending order. Use a list comprehension to generate the list of prime numbers.
"""

def product_of_primes(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [x for x in arr if is_prime(abs(x))]
    sorted_primes = sorted(primes, reverse=True)
    product = 1
    for i in range(min(4, len(sorted_primes))):
        product *= sorted_primes[i]
    return product
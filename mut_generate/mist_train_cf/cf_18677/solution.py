"""
QUESTION:
Create a function called `prime_product` that takes a list of integers as input. The function should return the product of the first four prime numbers in the list, sorted in descending order. The input list may contain both prime and non-prime numbers.
"""

def prime_product(arr):
    # Function to check if a number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # List comprehension to get prime numbers in descending order
    primes = [num for num in sorted(arr, reverse=True) if is_prime(num)]

    # Calculate the product of the first four prime numbers
    product = 1
    for num in primes[:4]:
        product *= num

    return product
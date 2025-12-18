"""
QUESTION:
Write a function `calculate_product_and_primes` that takes a list of positive integers as input. The function should return a tuple where the first element is the product of all unique prime numbers in the list, and the second element is a list of these unique prime numbers in descending order.
"""

def calculate_product_and_primes(numbers):
    primes = set()
    product = 1

    # Helper function to check if a number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in numbers:
        if is_prime(num) and num not in primes:
            primes.add(num)
            product *= num

    return product, sorted(list(primes), reverse=True)
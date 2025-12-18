"""
QUESTION:
Create a function `filter_and_find_primes` that takes a list of integers as input and returns a dictionary. The function should filter out the even numbers from the input list, identify the prime numbers from the remaining list, and create a dictionary where the key is a prime number and the value is a list of its divisors. The function should use an efficient algorithm for prime number detection and divisor generation.
"""

def filter_and_find_primes(numbers):
    def list_of_divisors(n):
        divisors = [1]
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                divisors.extend([i, n // i])
        if n not in divisors:
            divisors.append(n)
        return divisors

    # Filter out even numbers
    numbers = [n for n in numbers if n % 2 != 0]

    # Initialize prime dictionary
    primes = {}

    for n in numbers:
        # Prime numbers must be greater than 1
        if n > 1:
            for i in range(2, int(n**0.5) + 1):
                if (n % i) == 0:
                    break
            else:
                primes[n] = list_of_divisors(n)

    return primes
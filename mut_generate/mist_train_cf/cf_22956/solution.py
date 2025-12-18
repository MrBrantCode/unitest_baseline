"""
QUESTION:
Write a function `find_second_smallest_prime` that takes a list of integers as input and returns the second smallest prime number. The function should return `None` if the list contains less than two prime numbers.
"""

def find_second_smallest_prime(numbers):
    primes = []
    for num in numbers:
        if num < 2:
            continue
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
    primes.sort()
    return primes[1] if len(primes) >= 2 else None
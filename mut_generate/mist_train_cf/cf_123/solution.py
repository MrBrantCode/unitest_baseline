"""
QUESTION:
Write a function `get_first_five_primes(numbers)` that takes a list of integers `numbers` as input and returns the first 5 prime numbers from the list. The function should return a list of prime numbers in the order they appear in the input list. If the input list contains less than 5 prime numbers, the function should return all the prime numbers in the list.
"""

def get_first_five_primes(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
        if len(primes) == 5:
            break
    return primes
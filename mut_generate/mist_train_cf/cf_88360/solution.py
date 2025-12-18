"""
QUESTION:
Create a function `prime_numbers` that takes a positive integer `n` as input and returns a list of all prime numbers up to `n` in descending order. The function should have a time complexity of O(n^2 log n) and a space complexity of O(n).
"""

def prime_numbers(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    for num in range(n, 1, -1):
        if is_prime(num):
            primes.append(num)
    return primes
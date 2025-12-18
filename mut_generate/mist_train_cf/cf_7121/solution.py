"""
QUESTION:
Write a function `get_last_two_odd_primes(arr)` that takes an array of integers as input and returns an array of the last two odd prime numbers in the original order. If there are no odd prime numbers in the array, return an empty array.
"""

def get_last_two_odd_primes(arr):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    for num in arr[::-1]:
        if num % 2 != 0 and is_prime(num):
            primes.append(num)
            if len(primes) == 2:
                break
    primes.reverse()
    return primes
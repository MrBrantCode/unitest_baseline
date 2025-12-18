"""
QUESTION:
Write a function called `find_unique_primes` that takes a list of strings as input, where each string represents a number. The function should return a list of unique prime numbers in descending order, ignoring case sensitivity and only considering prime numbers within the range of 1 to 1000, inclusive.
"""

def find_unique_primes(nums):
    unique_primes = set()
    for num in nums:
        num = num.lower()
        if 1 <= int(num) <= 1000 and is_prime(int(num)):
            unique_primes.add(int(num))
    return sorted(unique_primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
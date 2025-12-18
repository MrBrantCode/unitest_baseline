"""
QUESTION:
Write a function `find_unique_primes` that takes a list of string numbers as input, finds the unique prime numbers within the range of 1 to 1000 (inclusive) while ignoring case sensitivity, and returns them in a list in descending order. The function should only consider the unique prime numbers.
"""

def find_unique_primes(nums):
    unique_primes = []
    seen = set()
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in nums:
        num = int(num.lower())
        if 1 <= num <= 1000 and is_prime(num) and num not in seen:
            unique_primes.append(num)
            seen.add(num)
    unique_primes.sort(reverse=True)
    return unique_primes
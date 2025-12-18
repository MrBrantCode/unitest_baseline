"""
QUESTION:
Find the number at a given index in a sorted descending array of prime numbers, which may include duplicates and negative prime numbers. The function should be named `find_prime_at_index`. The array will contain integers and the index will be a non-negative integer.
"""

def find_prime_at_index(nums, index):
    primes = set()
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in nums:
        if is_prime(abs(num)):
            primes.add(num)

    primes = sorted(list(primes), reverse=True)
    
    return primes[index]
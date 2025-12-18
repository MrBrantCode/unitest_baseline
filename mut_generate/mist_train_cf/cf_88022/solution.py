"""
QUESTION:
Write a function `generate_prime_numbers(start, end)` that generates a list of unique prime numbers between `start` and `end` (inclusive), sorted in ascending order, where `start` and `end` can be negative, and the range can be up to 10^9. The time complexity of the solution should be O(n log n), where n is the number of prime numbers in the range.
"""

def generate_prime_numbers(start, end):
    # Step 1
    isPrime = [True] * (end + 1)
    
    # Step 2
    p = 2
    
    # Step 3
    while p * p <= end:
        if isPrime[p]:
            for i in range(p * p, end + 1, p):
                isPrime[i] = False
        p += 1
    
    # Step 4
    primes = []
    for i in range(start, end + 1):
        # Step 5
        if i >= 2 and isPrime[i]:
            primes.append(i)
    
    # Step 6
    return primes
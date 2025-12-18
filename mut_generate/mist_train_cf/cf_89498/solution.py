"""
QUESTION:
Implement a recursive function named `reverse_sum_of_primes` that calculates the sum of prime numbers without repeating digits, where the number of prime numbers added to the sum is divisible by 3. The function should start from 2 and keep finding prime numbers until the sum is divisible by 3, then return the sum. The function should take two parameters: `count` representing the current number of prime numbers found, and `sum_of_primes` representing the current sum of prime numbers found.
"""

def reverse_sum_of_primes(count, sum_of_primes, prime=2, seen=None):
    if seen is None:
        seen = set()
    if count % 3 == 0 and sum_of_primes % 3 == 0:
        return sum_of_primes

    while True:
        if all(digit not in seen for digit in str(prime)) and is_prime(prime):
            seen.add(str(prime))
            result = reverse_sum_of_primes(count + 1, sum_of_primes + prime, prime + 1, seen)
            if result is not None:
                return result
        prime += 1

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
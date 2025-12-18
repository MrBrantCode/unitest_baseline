"""
QUESTION:
Create a function `calculate_sums_and_prime_diff` that takes an integer `n` as input and returns the sum of the first `n` odd integers, the sum of the first `n` even integers, the absolute difference between the sum of odd primes and even primes, the absolute difference between the sum of odd composites and even composites, the perfect square number closest to the absolute difference, the highest common factor of the sums of odd primes and even primes, and the highest common factor of the sums of odd composites and even composites.
"""

import math

def calculate_sums_and_prime_diff(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True

    odd_sum = sum(range(1, 2*n, 2))
    even_sum = sum(range(2, 2*n+1, 2))

    odd_primes = [x for x in range(1, odd_sum+1) if is_prime(x)]
    odd_composites = [x for x in range(1, odd_sum+1) if not is_prime(x)]
    even_primes = [x for x in range(1, even_sum+1) if is_prime(x)]
    even_composites = [x for x in range(1, even_sum+1) if not is_prime(x)]

    odd_prime_sum = sum(odd_primes)
    odd_composite_sum = sum(odd_composites)
    even_prime_sum = sum(even_primes)
    even_composite_sum = sum(even_composites)

    prime_diff = abs(odd_prime_sum - even_prime_sum)
    composite_diff = abs(odd_composite_sum - even_composite_sum)

    diff = min(prime_diff, composite_diff)
    closest_sq = round(math.sqrt(diff))**2

    hcf_odd_primes = math.gcd(odd_prime_sum, even_prime_sum)
    hcf_odd_composites = math.gcd(odd_composite_sum, even_composite_sum)

    return (odd_sum, even_sum, prime_diff, composite_diff, closest_sq, hcf_odd_primes, hcf_odd_composites)
"""
QUESTION:
Write a function `sort_integers` that takes a list of positive integers and an integer threshold as input, and returns the list sorted in ascending order based on the sum of their prime factors greater than or equal to the threshold. If the sums are equal, the list should be sorted based on the number of distinct prime factors of each element greater than or equal to the threshold. The function should handle lists with up to 10^6 elements efficiently.
"""

import sys

def sort_integers(numbers, threshold):
    def generate_prime_factors(n, threshold):
        factors = set()
        while n % 2 == 0:
            if 2 >= threshold:
                factors.add(2)
            n = n // 2
        for i in range(3, int(n**0.5) + 1, 2):
            while n % i == 0:
                if i >= threshold:
                    factors.add(i)
                n = n // i
        if n > 2 and n >= threshold:
            factors.add(n)
        return factors

    def calculate_sum_of_prime_factors(n, threshold):
        prime_factors = generate_prime_factors(n, threshold)
        return sum(prime_factors)

    def calculate_distinct_prime_factors(n, threshold):
        prime_factors = generate_prime_factors(n, threshold)
        return len(prime_factors)

    return sorted(numbers, key=lambda n: (calculate_sum_of_prime_factors(n, threshold), calculate_distinct_prime_factors(n, threshold)))
"""
QUESTION:
Calculate the sum of the first 100 odd and even numbers, classify these sums into odd and even prime and composite number components, compute the difference between the prime and composite sums, and find the perfect square number closest to this difference. Implement a function called `is_prime` to check if a number is prime and a function called `is_composite` to check if a number is composite.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def is_composite(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return True
    return False

def entrant():
    odd_sum = sum(range(1, 200, 2))
    even_sum = sum(range(2, 201, 2))

    odd_prime_sum = sum(i for i in range(1, odd_sum+1) if i % 2 == 1 and is_prime(i))
    odd_composite_sum = sum(i for i in range(1, odd_sum+1) if i % 2 == 1 and is_composite(i))

    even_prime_sum = sum(i for i in range(2, even_sum+1, 2) if is_prime(i))
    even_composite_sum = sum(i for i in range(2, even_sum+1, 2) if is_composite(i))

    prime_sum = odd_prime_sum + even_prime_sum
    composite_sum = odd_composite_sum + even_composite_sum
    diff = prime_sum - composite_sum

    closest_square = round(math.sqrt(abs(diff))) ** 2
    
    return odd_sum, even_sum, odd_prime_sum, odd_composite_sum, even_prime_sum, even_composite_sum, diff, closest_square
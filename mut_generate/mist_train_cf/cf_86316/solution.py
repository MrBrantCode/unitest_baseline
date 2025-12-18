"""
QUESTION:
Write a function named `find_unique_primes` that takes a list of integers as input and returns a tuple containing the number of unique prime numbers in the list, the largest prime number, and the smallest prime number. The function should not use any built-in functions or libraries to check for prime numbers, and its time complexity should be O(n), where n is the length of the list.
"""

import math

def find_unique_primes(numbers):
    prime_numbers = set()
    largest_prime = None
    smallest_prime = None
    
    for num in numbers:
        is_prime = True
        if num < 2:
            continue
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.add(num)
            
            if largest_prime is None or num > largest_prime:
                largest_prime = num
            if smallest_prime is None or num < smallest_prime:
                smallest_prime = num
    
    return len(prime_numbers), largest_prime, smallest_prime
"""
QUESTION:
Write a function `find_unique_primes` that takes a list of integers as input and returns a tuple containing three values: the number of unique prime numbers in the list, the largest prime number, and the smallest prime number. The function should not use any built-in functions or libraries to check for prime numbers, and it should have a time complexity of O(n), where n is the length of the list.
"""

import math

def find_unique_primes(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    prime_numbers = []
    largest_prime = None
    smallest_prime = None
    
    for num in numbers:
        if is_prime(num):
            if num not in prime_numbers:
                prime_numbers.append(num)
            
            if largest_prime is None or num > largest_prime:
                largest_prime = num
            if smallest_prime is None or num < smallest_prime:
                smallest_prime = num
    
    return len(prime_numbers), largest_prime, smallest_prime
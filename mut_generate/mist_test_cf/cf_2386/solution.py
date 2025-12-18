"""
QUESTION:
Write a function `process_prime_numbers` that takes a list of integers as input. This function should calculate the sum of all prime numbers in the list, the average of all prime numbers, the highest prime number, and the lowest prime number in the list. The function should return these four values. Assume that the input list contains at least one prime number. The function should not take any other parameters other than the list of integers.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def process_prime_numbers(numbers):
    prime_sum = 0
    primes = []
    
    for num in numbers:
        if is_prime(num):
            prime_sum += num
            primes.append(num)
    
    average_prime = prime_sum / len(primes)
    highest_prime = max(primes)
    lowest_prime = min(primes)
    
    return prime_sum, average_prime, highest_prime, lowest_prime
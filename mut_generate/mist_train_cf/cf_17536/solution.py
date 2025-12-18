"""
QUESTION:
Create a function `generate_prime_array(n)` that takes an integer `n` as input and returns an array of size `n` with distinct prime numbers. The function should have a time complexity of O(n) and a space complexity of O(n).
"""

import math

def generate_prime_array(n):
    prime_array = [0] * n  # Create an array of size n with values initialized to 0
    prime_nums = []  # Store the prime numbers
    
    # Initialize all elements in the array to be distinct prime numbers
    num = 2
    while len(prime_nums) < n:
        # Check if the number is prime
        is_prime = True
        for prime in prime_nums:
            if prime > math.isqrt(num):
                break
            if num % prime == 0:
                is_prime = False
                break
        
        # If the number is prime, add it to the prime_nums list and set it in the array
        if is_prime:
            prime_nums.append(num)
            prime_array[len(prime_nums) - 1] = num
        
        num += 1
    
    return prime_array
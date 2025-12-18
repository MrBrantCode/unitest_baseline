"""
QUESTION:
Create a function `classify_array(arr)` that takes an array of integers as input. The function should return a tuple containing three values: a boolean indicating whether the length of the array is even, a boolean indicating whether the array contains any prime numbers, and the average of all prime numbers found in the array. The function should be able to handle arrays with up to 10^6 elements efficiently.
"""

import math

def classify_array(arr):
    length = len(arr)
    is_even_length = length % 2 == 0
    
    has_prime_numbers = False
    prime_sum = 0
    prime_count = 0
    
    for num in arr:
        if num <= 1:
            continue
        
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            has_prime_numbers = True
            prime_sum += num
            prime_count += 1
    
    average_prime = prime_sum / prime_count if prime_count > 0 else 0
    
    return is_even_length, has_prime_numbers, average_prime
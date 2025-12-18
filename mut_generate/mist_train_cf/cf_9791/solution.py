"""
QUESTION:
Create a function `categorize_numbers` that takes an array of numbers as input, categorizes them into prime and composite numbers, and returns the prime numbers, composite numbers, and their respective counts. The function should ignore duplicate numbers in the array and handle negative numbers.
"""

import math

def categorize_numbers(arr):
    prime_numbers = []
    composite_numbers = []
    prime_count = 0
    composite_count = 0
    
    unique_numbers = list(set(arr))
    
    for num in unique_numbers:
        if num < 2:
            continue
        is_composite = False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_composite = True
                break
        if is_composite:
            composite_numbers.append(num)
            composite_count += 1
        else:
            prime_numbers.append(num)
            prime_count += 1
    
    return prime_numbers, composite_numbers, prime_count, composite_count
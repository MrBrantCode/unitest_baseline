"""
QUESTION:
Create a function `categorize_numbers` that takes an array of integers as input. The function should categorize the numbers in the array into prime and composite numbers, ignoring any duplicates and negative numbers. It should return the list of prime numbers, the list of composite numbers, the count of prime numbers, and the count of composite numbers. The array can contain negative numbers and duplicates.
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
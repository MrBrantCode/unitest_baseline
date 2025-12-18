"""
QUESTION:
Create a function `reorder_array(arr)` that takes an array of integers as input and returns the array reordered such that all non-prime numbers appear before prime numbers, while maintaining their relative order within each group.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def reorder_array(arr):
    prime_numbers = []
    non_prime_numbers = []
    
    for num in arr:
        if is_prime(num):
            prime_numbers.append(num)
        else:
            non_prime_numbers.append(num)
    
    return non_prime_numbers + prime_numbers
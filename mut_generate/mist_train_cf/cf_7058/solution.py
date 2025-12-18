"""
QUESTION:
Create a function `classify_array(arr)` that classifies the input array as having an even or odd length and determines if it contains any prime numbers. The function should also return the average of all the prime numbers found in the array. The function should be able to handle arrays with a size of up to 10^6 elements efficiently. The input array `arr` contains integers and the function should return a tuple of three values: a boolean indicating whether the array has an even length, a boolean indicating whether the array contains prime numbers, and the average of the prime numbers.
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
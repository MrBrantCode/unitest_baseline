"""
QUESTION:
Create a function named `classify_array` that takes an array of integers as input. The function should return a tuple containing three values: 
- A boolean indicating whether the array has an even length.
- A boolean indicating whether the array contains any prime numbers.
- The average of all the prime numbers found in the array (or None if no prime numbers are found).
The function should consider prime numbers as numbers greater than 1 that have no divisors other than 1 and themselves.
"""

import math

def classify_array(arr):
    length = len(arr)
    is_even_length = length % 2 == 0
    
    has_prime = False
    prime_sum = 0
    prime_count = 0
    
    for num in arr:
        if num > 1:
            is_prime = True
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                has_prime = True
                prime_sum += num
                prime_count += 1
                
    if prime_count > 0:
        prime_average = prime_sum / prime_count
    else:
        prime_average = None
    
    return is_even_length, has_prime, prime_average
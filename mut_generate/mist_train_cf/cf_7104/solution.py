"""
QUESTION:
Create a function `generate_sequence(start, end)` that generates a sequence of integers from `start` (k) to `end` (n) in the format `[k, k^2, k^3, ..., n^2, n^3]` and checks for prime numbers within the sequence. The function should return two lists: `sequence` containing the generated sequence and `prime_numbers` containing the prime numbers within the sequence. 

Restrictions: The prime number checking algorithm should have a time complexity of O(sqrt(n)). The sequence and prime numbers should be generated and returned separately.
"""

import math

def generate_sequence(k, n):
    sequence = []
    prime_numbers = []
    
    for num in range(k, n + 1):
        sequence.append(num**2)
        sequence.append(num**3)
        
        if num >= 2 and (num == 2 or num % 2 != 0) and all(num % i != 0 for i in range(3, int(math.sqrt(num)) + 1, 2)):
            prime_numbers.append(num)
    
    return sequence, prime_numbers
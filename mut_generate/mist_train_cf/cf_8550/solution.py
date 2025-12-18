"""
QUESTION:
Implement a function `get_prime_numbers` that takes two parameters, `lower_bound` and `upper_bound`, and returns a list of prime numbers in the range from `lower_bound` to `upper_bound` (inclusive) excluding the number 13. The function should achieve a time complexity of O(log n), where n is the size of the range.
"""

import math

def get_prime_numbers(lower_bound, upper_bound):
    prime_numbers = []
    for num in range(lower_bound, upper_bound + 1):
        if num == 13:
            continue
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    return prime_numbers
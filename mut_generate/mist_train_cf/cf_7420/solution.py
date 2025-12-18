"""
QUESTION:
Create a function called `find_second_highest_prime` that takes a list of integers as input and returns the second highest prime number from the list. The function should handle both positive and negative integers, as well as zero. If there is no second highest prime number, the function should return -1.
"""

import math

def find_second_highest_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    primes = [num for num in numbers if is_prime(abs(num))]
    primes.sort(reverse=True)
    
    if len(primes) < 2:
        return -1
    
    return primes[1]
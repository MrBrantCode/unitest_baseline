"""
QUESTION:
Create a function named `filter_prime_numbers` that takes a list of integers as input and returns a new list containing only the prime numbers from the input list. The function should have a time complexity of O(n√m), where n is the length of the input list and m is the maximum value in the input list. The space complexity should be O(1), excluding the space required to store the filtered numbers in the new list. The solution should not use any built-in functions or libraries that directly solve the problem.
"""

import math

def filter_prime_numbers(numbers):
    primes = []
    
    for number in numbers:
        is_prime = True
        
        # Check divisibility from 2 to square root of the number
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                is_prime = False
                break
        
        if is_prime and number > 1:  # number should be greater than 1
            primes.append(number)
    
    return primes
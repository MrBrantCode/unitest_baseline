"""
QUESTION:
Create a function called `find_prime_numbers` that takes a list of integers as input and returns a new list containing only the prime numbers greater than 100 in ascending order. The time complexity of the function should be O(n√m), where n is the length of the input list and m is the maximum value in the input list.
"""

import math

def find_prime_numbers(numbers):
    prime_numbers = []
    for num in numbers:
        if num > 100:
            is_prime = True
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(num)
    prime_numbers.sort()
    return prime_numbers
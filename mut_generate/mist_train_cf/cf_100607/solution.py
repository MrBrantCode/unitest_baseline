"""
QUESTION:
Create a function called `prime_composite_table` that takes in a list of integers as input and returns a table where each row contains a number from the input list and its corresponding classification as either "Prime" or "Composite". Assume that prime numbers are numbers greater than 1 that have no divisors other than 1 and themselves, and composite numbers are numbers with at least one divisor other than 1 and themselves.
"""

import math

def prime_composite_table(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True

    table = []
    for num in nums:
        classification = "Prime" if is_prime(num) else "Composite"
        table.append([num, classification])
    return table
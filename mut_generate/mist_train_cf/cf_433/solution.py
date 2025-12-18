"""
QUESTION:
Write a function `sum_of_primes_in_range` that takes two integers `start` and `end` as input and returns the sum of all prime numbers in the range from `start` to `end` (inclusive). The function should use a list comprehension to generate the prime numbers. The prime number check should be performed within the list comprehension.
"""

def sum_of_primes_in_range(start, end):
    return sum([num for num in range(start, end+1) if all(num%i!=0 for i in range(2,num))])
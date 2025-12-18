"""
QUESTION:
Create a function `filter_primes(nums)` that takes a list of integers as input and returns a new list containing only the prime numbers from the original list. The function should only consider numbers greater than 1 as potential primes and should only check for divisibility up to the square root of each number.
"""

def filter_primes(nums):
    primes = []
    for num in nums:
        if num > 1: 
            for i in range(2, int(num**0.5) + 1): 
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes
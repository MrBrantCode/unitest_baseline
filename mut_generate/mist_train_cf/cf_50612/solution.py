"""
QUESTION:
Create a function `extract_prime(nums)` that takes a list of integers as input and returns a new list containing only the prime numbers from the input list in descending order. The function should not use any pre-built library functions.
"""

def extract_prime(nums):
    primes = []
    for num in nums:
        if num > 1:  
            for i in range(2, num):
                if (num % i) == 0:  
                    break
            else:
                primes.append(num)
    primes.sort(reverse=True)  
    return primes
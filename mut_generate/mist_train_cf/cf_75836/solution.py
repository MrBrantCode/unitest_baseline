"""
QUESTION:
Write a function `filter_primes` that takes a list of numbers as input, filters out prime numbers, and stops checking once it encounters a non-numeric value. The function should consider integers only and exclude negative integers, floating point numbers, and non-numeric values. The function should return a list of prime numbers found in the input list.
"""

def filter_primes(nums):
    def is_prime(n):
        if n < 2:  
            return False
        for i in range(2, int(n**0.5) + 1):  
            if n % i == 0:  
                return False
        return True

    primes = []
    for num in nums:
        if isinstance(num, int) and is_prime(num):
            primes.append(num)
        elif not isinstance(num, (int, float)):  
            break
    return primes
"""
QUESTION:
Write a function named `count_frequency_and_primes` that takes a list of integers between 1 and 1000 (inclusive) as input. The function should return a tuple containing a dictionary where keys are distinct elements from the input list and their corresponding values are the occurrence frequencies, and a list of prime numbers found in the input list. A number is considered prime if it is only divisible by 1 and itself.
"""

def count_frequency_and_primes(lst):
    import math
    def is_prime(n):
        if n == 1: return False
        if n == 2: return True
        if n % 2 == 0: return False
        for current in range(3, math.isqrt(n) + 1, 2):
            if n % current == 0: return False
        return True
    
    freq_dict = {}
    primes = []
    
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
        
        if is_prime(num):
            primes.append(num)
            
    return freq_dict, primes
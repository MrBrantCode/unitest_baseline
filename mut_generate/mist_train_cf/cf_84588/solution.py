"""
QUESTION:
Write a function called `find_prime_sums(n)` that calculates the collective sum of all unique prime numbers derived from the number of unique ways to ascend a staircase of `n` steps, where each step can be either 1 or 2 steps at a time. The function should consider all possible staircases from 0 to `n` steps and return their corresponding unique prime sums.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**(0.5)) + 1):
        if n % i == 0:
            return False
    return True

def count_ways(n, memo = {}):
    if n == 1 or n == 0: 
        return 1
    elif n in memo:
        return memo[n]
    else:
        result = count_ways(n - 1, memo) + count_ways(n - 2, memo)
        memo[n] = result
        return result

def find_prime_sums(n): 
    prime_sum = 0 
    for i in range(n+1): 
        unique_ways = count_ways(i) 
        if is_prime(unique_ways): 
            prime_sum += unique_ways 
      
    return prime_sum
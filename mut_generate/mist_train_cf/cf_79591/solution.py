"""
QUESTION:
Design a function `prime_positions` that, given a list of integers, returns a list of prime numbers and their positions in the original list. The function should handle large numbers (up to 10^9) efficiently and utilize optimization techniques such as memoization or dynamic programming. Additionally, describe the time complexity of the algorithm and explain the approach to optimizing its computational performance. Assume the input is a list of non-negative integers.
"""

def is_prime(n, memo):
    """Function to check if a number is prime or not."""
    if n in memo:
        return memo[n]
    if n <= 1:
        return False
    if n == 2:
        return True

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            memo[n] = False
            return False
            
    memo[n] = True
    return True

def prime_positions(lst):
    """Function to find prime numbers and their positions."""
    memo = dict() # to store known prime numbers
    primes = []    # list of primes
    pos = []       # position of primes in original list
    for idx, n in enumerate(lst):
        if is_prime(n, memo):
            primes.append(n)
            pos.append(idx)
    return primes, pos
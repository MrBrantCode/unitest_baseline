"""
QUESTION:
Create a function named `is_prime(n)` to determine whether a given number `n` is a prime number using the Sieve of Eratosthenes algorithm. The function should take an integer `n` as input and return a boolean value (`True` if `n` is prime, `False` otherwise) without considering any numbers less than or equal to 1.
"""

def is_prime(n): 
    if n <= 1: 
        return False
  
    # create a list of all numbers from 0 to n
    nums = [True for _ in range(n + 1)] 
  
    p = 2
    while (p * p <= n): 
        # If prime[p] is not changed, it is a prime 
        if nums[p] is True: 

            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                nums[i] = False
        p += 1

    return nums[n]
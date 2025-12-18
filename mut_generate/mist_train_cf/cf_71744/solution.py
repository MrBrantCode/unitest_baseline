"""
QUESTION:
Create a function named `is_prime` that takes an integer `n` as input and returns a string indicating whether `n` is 'Prime' or 'Composite'. The function should use the 6k ± 1 optimization and only check up to the square root of `n`. The function should handle negative numbers, 0, and 1, which are not prime numbers.
"""

def is_prime(n):
    """Check if a number is Prime or Composite"""
    
    # negatives, 0, and 1 are not primes
    if n < 2:
        return f'{n} is not prime'
    
    # 2 and 3 are primes
    elif n == 2 or n == 3:
        return f'{n} is Prime'
    
    # multiples of 2 and 3 are not primes
    elif n % 2 == 0 or n % 3 == 0:
        return f'{n} is Composite'
    
    # we only need to check up to sqrt(n)
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return f'{n} is Composite'
        
        # this will check (6k - 1) and (6k + 1)
        i += w
        w = 6 - w
    
    return f'{n} is Prime'
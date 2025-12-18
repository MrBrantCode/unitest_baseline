"""
QUESTION:
Write a function `is_perfect_square_and_prime_root` that takes an integer `n` as input and returns a tuple of two boolean values. The first value indicates whether `n` is a perfect square, and the second value indicates whether the square root of `n` is a prime number. Do not use any built-in Python functions or libraries for the prime number check. The function should consider edge cases and include comments for clarity.
"""

def is_perfect_square_and_prime_root(n):
    # Compute square root and store as variable 'sqrt'
    sqrt = n ** 0.5
    
    # Check if 'sqrt' is an integer
    is_perfect_square = sqrt == int(sqrt)
    
    # Special case: 1 is not a prime number
    if n == 1:
        is_prime_root = False
    # Special case: 2 is a prime number
    elif n == 4:
        is_prime_root = True
    else:
        # Start from 2 and iterate up to the square root of 'sqrt' (or n ** 0.25)
        is_prime_root = True
        if is_perfect_square:
            for i in range(2, int(sqrt ** 0.5) + 1):
                # If 'sqrt' is divisible by any number in this range, it's not prime
                if sqrt % i == 0:
                    is_prime_root = False
                    break
    
    # Return as tuple
    return (is_perfect_square, is_prime_root)
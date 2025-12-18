"""
QUESTION:
Create a function `get_prime_numbers(a, b)` that takes two integers `a` and `b` as input and returns a tuple containing a list of all prime numbers between `a` and `b` (inclusive) and the count of prime numbers in that range. The function should handle edge cases where `a` or `b` is negative, or `a` is greater than `b`.
"""

def get_prime_numbers(a, b):
    # Handle edge cases
    if a < 0 or b < 0:
        return "Invalid input. Please enter non-negative values."
    elif a > b:
        return "Invalid input. The start number should be less than or equal to the end number."

    primes = []
    for num in range(a, b + 1):
       # all prime numbers are greater than 1
       if num > 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               primes.append(num)
    return primes, len(primes)
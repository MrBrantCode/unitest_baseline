"""
QUESTION:
Write a function named `prime_numbers` that generates a list of prime numbers within a specified range, inclusive of the end values. The function should take two parameters, `lower` and `upper`, representing the start and end of the range, and return a list of prime numbers within this range.
"""

def prime_numbers(lower, upper):
    primes = []
    for num in range(lower, upper + 1):
       if num > 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               primes.append(num)
    return primes
"""
QUESTION:
Write a function named `largest_prime_factor` that takes a single argument `number` and returns the largest prime factor of the given number. The function should be efficient and handle large inputs. Note that the function should only return the largest prime factor, not all prime factors.
"""

def largest_prime_factor(number):
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
    if number > 1:
        return number
    return i
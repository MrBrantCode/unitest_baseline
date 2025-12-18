"""
QUESTION:
Write a function `find_prime_numbers` that takes a range defined by `start` and `end` as input and returns a list of distinct prime numbers within that range. The function should be able to handle any range of positive integers. Note that the prime numbers in the output list must be distinct and the list should not exceed 8 elements.
"""

def find_prime_numbers(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes[:8]  # Return only the first 8 distinct prime numbers
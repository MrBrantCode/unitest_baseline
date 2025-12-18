"""
QUESTION:
Write a Lambda function `filter_primes` that takes a list of integers as input, filters out the prime numbers, and returns a new list containing only the prime numbers. The function should handle negative integers by treating them as their positive counterparts when determining primality. Implement the primality check without using any built-in functions or libraries. Assume the input list contains only integers and has a length of 1000 or less.
"""

def filter_primes(lst):
    def is_prime(num):
        if num < 2:
            return False
        return all(num % i != 0 for i in range(2, int(num**0.5) + 1))

    return list(filter(lambda x: is_prime(abs(x)), lst))
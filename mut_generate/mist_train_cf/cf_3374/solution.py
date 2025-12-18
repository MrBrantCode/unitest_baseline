"""
QUESTION:
Create a function named `get_prime_numbers` that takes a list of integers as input and returns a new list containing only the prime numbers from the input list. The function should handle negative numbers and duplicates in the input list.
"""

def get_prime_numbers(lst):
    primes = set()
    for num in lst:
        if num > 1:
            for i in range(2, int(num/2)+1):
                if num % i == 0:
                    break
            else:
                primes.add(num)
    return list(primes)
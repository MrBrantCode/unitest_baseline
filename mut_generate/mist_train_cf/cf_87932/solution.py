"""
QUESTION:
Create a function `get_prime_numbers` that takes a list of integers as input. This function should return a new list containing only the prime numbers from the input list. The input list can contain negative numbers and duplicates.
"""

def get_prime_numbers(lst):
    primes = []
    for num in lst:
        if num > 1:
            for i in range(2, int(num/2)+1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes
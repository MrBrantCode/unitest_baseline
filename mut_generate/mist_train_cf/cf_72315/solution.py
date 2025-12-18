"""
QUESTION:
Write a function `prime_pairs_composite` that takes a list of unique prime numbers as input and returns `True` if the sum of any pair of primes is a composite number, and `False` otherwise. The function should not take any additional parameters other than the list of prime numbers.
"""

def is_composite(n):
    if n < 2: 
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False

def prime_pairs_composite(prime_list):
    for i in range(len(prime_list)):
        for j in range(i+1, len(prime_list)):
            if is_composite(prime_list[i] + prime_list[j]):
                return True
    return False
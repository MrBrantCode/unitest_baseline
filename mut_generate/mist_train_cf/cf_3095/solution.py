"""
QUESTION:
Create a function called `create_sorted_dict` that takes a dictionary of integers as input and returns a dictionary and a list of tuples. The dictionary should have the same keys as the input dictionary, but the values should be the sum of the prime factors of each key. The list of tuples should contain the same key-value pairs as the dictionary, sorted in ascending order based on the sum of the prime factors. The function should be able to handle keys up to 10^6.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_prime_factors(n):
    factors = []
    i = 2
    while i <= n:
        if is_prime(i) and n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    return sum(factors)

def create_sorted_dict(num_dict):
    sorted_list = sorted(num_dict.items(), key=lambda x: sum_prime_factors(x[0]))
    return dict(sorted_list), sorted_list
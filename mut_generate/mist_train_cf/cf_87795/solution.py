"""
QUESTION:
Write a function `create_sorted_dict` that takes a dictionary `num_dict` as input, where keys are integers up to 10^6. The function should return a tuple containing a dictionary and a list of tuples. The dictionary should have the same keys as the input dictionary, but the values should be the sum of the prime factors of each key. The list of tuples should contain the key-value pairs of the dictionary, sorted in ascending order based on the sum of the prime factors.
"""

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

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def create_sorted_dict(num_dict):
    return dict(sorted(num_dict.items(), key=lambda x: sum_prime_factors(x[0]))), sorted(num_dict.items(), key=lambda x: sum_prime_factors(x[0]))
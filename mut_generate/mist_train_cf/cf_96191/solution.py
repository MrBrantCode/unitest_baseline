"""
QUESTION:
Create a function `add_prime_dict` that takes two dictionaries `d1` and `d2` as input, where keys are positive integers between 2 and 100 (inclusive) and values are multiples of 5 between 10 and 500 (inclusive). The function should return a new dictionary containing only key-value pairs from `d1` and `d2` where keys are prime numbers and values are not divisible by 10 or 25. The resulting dictionary should be sorted in ascending order based on the keys.
"""

def add_prime_dict(d1, d2):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_divisible(num, div):
        if num % div == 0:
            return True
        return False

    result = {}
    for key in d1:
        if is_prime(key) and not is_divisible(d1[key], 10) and not is_divisible(d1[key], 25):
            result[key] = d1[key]
    for key in d2:
        if is_prime(key) and not is_divisible(d2[key], 10) and not is_divisible(d2[key], 25):
            result[key] = d2[key]

    return dict(sorted(result.items()))
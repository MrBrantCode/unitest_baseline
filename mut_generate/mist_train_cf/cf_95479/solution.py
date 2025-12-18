"""
QUESTION:
Create a function `create_mapping(dictionary)` that takes a dictionary as input, where the function returns a new dictionary with all keys in uppercase and values as positive integers. The function should only include keys that start with a vowel (a, e, i, o, u) and the sum of all values in the resulting dictionary must be a prime number. The function should run in O(n) time complexity, where n is the length of the dictionary.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def create_mapping(dictionary):
    mapping = {}
    total_sum = 0

    for key, value in dictionary.items():
        if key[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            if isinstance(value, int) and value > 0:
                mapping[key.upper()] = value
                total_sum += value

    if is_prime(total_sum):
        return mapping
    else:
        return {}
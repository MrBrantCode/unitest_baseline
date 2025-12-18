"""
QUESTION:
Create a function `create_mapping(dictionary)` that takes a dictionary as input and returns a dictionary where all keys are uppercase and all values are positive integers. The function should only include keys that start with a vowel (A, E, I, O, U) in the resulting dictionary. Additionally, the function should ensure that the sum of all values in the resulting dictionary is a prime number. The function should have a time complexity of O(n), where n is the length of the dictionary.
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
        key = key.upper()
        value = abs(int(value))
        if key[0] in 'AEIOU':
            mapping[key] = value
            total_sum += value

    while not is_prime(total_sum):
        total_sum += 1

    return mapping
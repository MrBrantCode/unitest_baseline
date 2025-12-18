"""
QUESTION:
Create a function named `create_mapping` that takes a dictionary as input and returns a new dictionary with all keys converted to uppercase, all values converted to positive integers, and only keys that start with a vowel included. The sum of all values in the new dictionary should be a prime number. Implement the function with a time complexity of O(n), where n is the length of the dictionary.
"""

def create_mapping(dictionary):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

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
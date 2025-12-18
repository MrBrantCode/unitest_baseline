"""
QUESTION:
Create a function `create_mapping(dictionary)` that takes a dictionary as input and returns a new dictionary with keys in uppercase and values as positive integers. The new dictionary should only include key-value pairs where the key starts with a vowel ('a', 'e', 'i', 'o', 'u'). Additionally, the function should only return the new dictionary if the sum of all values is a prime number; otherwise, it should return an empty dictionary.
"""

def create_mapping(dictionary):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    mapped_dict = {}
    sum_values = 0

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for key, value in dictionary.items():
        if key.lower()[0] in vowels:
            if isinstance(value, int) and value > 0:
                mapped_dict[key.upper()] = value
        if isinstance(value, int) and value > 0:
            sum_values += value

    if is_prime(sum_values):
        return mapped_dict
    else:
        return {}
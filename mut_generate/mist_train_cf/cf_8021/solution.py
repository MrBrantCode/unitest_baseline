"""
QUESTION:
Write a function `swap_vowel_prime_greater_than_ten` that takes a dictionary as input and returns a new dictionary where key-value pairs are swapped for keys that start with a vowel, have values that are prime numbers, and values that are greater than 10.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def swap_vowel_prime_greater_than_ten(dictionary):
    vowels = ['a', 'e', 'i', 'o', 'u']
    swapped_dict = dictionary.copy()
    for key, value in dictionary.items():
        if key[0].lower() in vowels and is_prime(value) and value > 10:
            swapped_dict[value] = key
            del swapped_dict[key]
    return swapped_dict
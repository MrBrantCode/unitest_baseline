"""
QUESTION:
Create a function named `swap_vowel_prime` that takes a dictionary as input. The function should swap key-value pairs in the dictionary only for keys that start with a vowel (a, e, i, o, u) and have values that are prime numbers. The function should return the modified dictionary.
"""

import math

def swap_vowel_prime(dictionary):
    vowels = ['a', 'e', 'i', 'o', 'u']
    primes = []

    # Find prime numbers
    for num in dictionary.values():
        if num > 1:
            for i in range(2, int(math.sqrt(num)) + 1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)

    # Swap key-value pairs
    swapped_dict = {}
    for key, value in dictionary.items():
        if key[0].lower() in vowels and value in primes:
            swapped_dict[value] = key
        else:
            swapped_dict[key] = value

    return swapped_dict
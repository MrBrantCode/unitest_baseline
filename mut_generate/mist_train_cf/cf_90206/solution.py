"""
QUESTION:
Create a function called `swap_vowel_prime_greater_than_ten` that takes a dictionary as input and returns the dictionary with key-value pairs swapped, but only for keys that start with a vowel (case-insensitive) and values that are prime numbers greater than 10. Note that the prime numbers greater than 10 should also be present as values in the original dictionary.
"""

def swap_vowel_prime_greater_than_ten(dictionary):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    vowels = 'aeiou'
    swapped_dict = dictionary.copy()
    for key, value in dictionary.items():
        if key[0].lower() in vowels and is_prime(value) and value > 10 and value in swapped_dict.values():
            swapped_dict[value] = key
            del swapped_dict[key]
    return swapped_dict
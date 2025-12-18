"""
QUESTION:
Implement a function `custom_hash(my_str, prime_number)` that generates a unique integer key by applying a custom hash function to the input string `my_str` and a given prime number `prime_number`. The custom hash function should not use any existing Python built-in hash functions or libraries. The function should take into account the position of characters in the string to minimize hash collisions.
"""

def custom_hash(my_str, prime_number):
    hash_value = 0

    for index, char in enumerate(my_str):
        hash_value += (index + 1) * ord(char) * prime_number

    return hash_value
"""
QUESTION:
Create a function named `merge_and_sort_dict` that takes two dictionaries `dict1` and `dict2` as input, where the keys are positive integers greater than 1 and less than or equal to 1000, and the values are multiples of 5 greater than or equal to 10 and less than or equal to 1000. The function should return a new dictionary where the keys are prime numbers, the values are not divisible by 10 or 25, and the dictionary is sorted in descending order based on the values.
"""

import math

def merge_and_sort_dict(dict1, dict2):
    # Function to check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    # Create a new dictionary by adding the values of dict1 and dict2
    new_dict = {}
    for key in dict1:
        if is_prime(key) and dict1[key] % 10 != 0 and dict1[key] % 25 != 0:
            new_dict[key] = dict1[key]
    for key in dict2:
        if is_prime(key) and dict2[key] % 10 != 0 and dict2[key] % 25 != 0:
            new_dict[key] = dict2[key]

    # Sort the new dictionary in descending order based on the values
    sorted_dict = dict(sorted(new_dict.items(), key=lambda x: x[1], reverse=True))

    return sorted_dict
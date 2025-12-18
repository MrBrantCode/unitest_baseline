"""
QUESTION:
Create a dictionary `create_prime_dict` from two given lists, `list1` and `list2`, with the following restrictions:
- `list1` and `list2` have the same length.
- Each element in `list1` is a string consisting of only lowercase alphabetic characters.
- Each element in `list2` is a positive integer not exceeding 100.
- The sum of all integers in `list2` is a prime number.
- The keys in the dictionary should be sorted in descending order based on the length of the corresponding strings in `list1`.
- If the sum of `list2` is not a prime number, return an empty dictionary.
- If the lengths of `list1` and `list2` are not the same, return an empty dictionary.
"""

import math

def create_prime_dict(list1, list2):
    # Check if the lengths of list1 and list2 are the same
    if len(list1) != len(list2):
        return {}

    # Check if the sum of list2 is prime
    sum_list2 = sum(list2)
    is_prime = True
    for i in range(2, int(math.sqrt(sum_list2)) + 1):
        if sum_list2 % i == 0:
            is_prime = False
            break

    # If the sum is prime, create the dictionary
    if not is_prime:
        return {}

    # Sort list1 and list2 based on the length of strings in list1 in descending order
    sorted_lists = sorted(zip(list1, list2), key=lambda x: len(x[0]), reverse=True)

    # Create the dictionary
    prime_dict = {}
    for string, num in sorted_lists:
        prime_dict[string] = num

    return prime_dict
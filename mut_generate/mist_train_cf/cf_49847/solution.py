"""
QUESTION:
Create a function `cubic_roots_dict` that takes a list of numbers as an argument and returns a dictionary. The dictionary should contain each number in the list as a key, with its cube root as the value unless the number is prime, in which case its square root should be the value. The function should efficiently handle large input lists. The function should also round the cube root to 5 decimal places.
"""

import math

def cubic_roots_dict(lst):
    def is_prime(n):
        if n == 1 or n == 0: return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0: return False
        return True

    roots = {}
    for num in lst:
        if is_prime(num):
            roots[num] = math.sqrt(num)
        else:
            roots[num] = round(num ** (1. / 3.), 5)  # cube root

    return roots
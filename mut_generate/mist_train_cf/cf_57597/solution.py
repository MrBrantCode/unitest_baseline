"""
QUESTION:
Write a function `prime_and_factorial` that takes a list of integers as input, identifies the prime numbers, calculates their factorial values, and returns a dictionary where the keys are the prime numbers and the values are their corresponding factorial values. The function should handle non-integer values in the list by skipping them and should be able to handle large integers efficiently.
"""

import math

def prime_and_factorial(num_list):
    result = {}

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

    try:
        for num in num_list:
            if not isinstance(num, int):
                print(f"{num} is not an integer. Skipping...")
                continue
            if is_prime(num):
                result[num] = math.factorial(num)
        return result
    except TypeError:
        print("Please provide a list of integers.")
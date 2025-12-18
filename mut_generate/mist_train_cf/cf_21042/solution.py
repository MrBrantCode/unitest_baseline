"""
QUESTION:
Write a function `count_prime_numbers_with_3(lst)` that takes a list of positive integers as input and returns the count of numbers in the list that are prime and contain the digit 3. The time complexity of the function should not exceed O(n log(log n)), where n is the number of elements in the list.
"""

import math

def count_prime_numbers_with_3(lst):
    count = 0

    def is_prime_and_contains_3(num):
        if num < 2:
            return False
        if '3' not in str(num):
            return False

        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False

        return True

    for num in lst:
        if is_prime_and_contains_3(num):
            count += 1

    return count
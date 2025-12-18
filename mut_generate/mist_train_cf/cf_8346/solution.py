"""
QUESTION:
Create a function called `find_second_largest_prime` that takes a pandas Series `A` as input and returns the second largest prime number in the series. The function should have a time complexity of O(nlogn), where n is the number of elements in the series. The function should also handle cases where there are less than two prime numbers in the series.
"""

import pandas as pd
import numpy as np

def find_second_largest_prime(A):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(np.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    largest_prime = 0
    second_largest_prime = 0

    for num in A.values:
        if is_prime(num):
            if num > largest_prime:
                second_largest_prime = largest_prime
                largest_prime = num
            elif num > second_largest_prime and num != largest_prime:
                second_largest_prime = num

    return second_largest_prime
"""
QUESTION:
Write a function named `smallest_triangular_position(n)` that calculates the position of the smallest triangular number with n digits and returns the number, its position, and the time taken to compute the result. The function should be able to handle a single integer or a list of integers as input. It should also be able to handle large inputs efficiently (up to 10^6), and provide error handling for non-positive integers, non-integer inputs, and cases where no triangular number is found for the provided digit count.
"""

import math
import time

def smallest_triangular_position(n):
    if isinstance(n, list):
        result = []
        for num in n:
            result.append(smallest_triangular_position(num))
        return result
    else:
        if n <= 0:
            return "Error: n should be a positive integer"
        if not isinstance(n, int):
            n = round(n)
        start_time = time.time()
        low = 1
        high = int(10e6)  # upper limit for processing

        def triangular_number(x):
            return x * (x + 1) // 2

        def binary_search(n, low, high):
            if high >= low:
                mid = (high + low) // 2
                mid_number_log = math.log10(triangular_number(mid))

                if mid_number_log >= n:
                    if mid_number_log - 1 < n:
                        return mid
                    else:
                        return binary_search(n, low, mid - 1)
                else:
                    return binary_search(n, mid + 1, high)
            else:
                return -1

        index = binary_search(n, low, high)

        if index != -1:
            execution_time = time.time() - start_time
            triangular = triangular_number(index)
            return triangular, index, round(execution_time, 4)
        else:
            return "No triangular number found for provided digit count"
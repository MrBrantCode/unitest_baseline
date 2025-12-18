"""
QUESTION:
Implement a function named `solve` that accepts an array of integers, removes duplicates, and sorts the unique elements according to the following custom rules:
- Perfect squares in ascending order first
- Even numbers (excluding perfect squares) in ascending order next
- Odd numbers (excluding perfect squares) in ascending order last
Additionally, return the sum of all the perfect squares in the array.
"""

import math

def solve(arr):
    square_arr, even_arr, odd_arr = [], [], []
    square_sum = 0

    for num in set(arr):
        sqrt_num = math.sqrt(num)

        if sqrt_num.is_integer():
            square_arr.append(num)
            square_sum += num
        elif num % 2 == 0:
            even_arr.append(num)
        else:
            odd_arr.append(num)

    square_arr.sort()
    even_arr.sort()
    odd_arr.sort()

    return square_arr + even_arr + odd_arr, square_sum
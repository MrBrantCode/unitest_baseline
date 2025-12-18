"""
QUESTION:
Implement a recursive function `sum_of_squares_even` that takes an array of positive integers as input and returns a tuple containing the sum of the squares of all even numbers in the array and the count of even numbers in the array. The array has a length of at most 100.
"""

def sum_of_squares_even(arr):
    if len(arr) == 0:
        return 0, 0

    sum_of_squares, count = sum_of_squares_even(arr[1:])

    if arr[0] % 2 == 0:
        sum_of_squares += arr[0] ** 2
        count += 1

    return sum_of_squares, count
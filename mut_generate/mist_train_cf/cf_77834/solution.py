"""
QUESTION:
Write a function `solve_problem` that takes an array of integers as input. The function should sort the array in descending order, remove any numbers that are multiples of 5, convert the remaining numbers into a string with each number separated by a comma, and surround the string with square brackets.
"""

def entance(arr):
    # 1. Sort the array in descending order
    arr.sort(reverse=True)

    # 2. Remove all numbers which are multiple of 5
    arr = [x for x in arr if x % 5 != 0]

    # 3. Transform the resulting array into a string delineated by commas
    str_arr = ', '.join(map(str, arr))

    # 4. Add surrounding square brackets to the string.
    str_arr = '[' + str_arr + ']'
    return str_arr
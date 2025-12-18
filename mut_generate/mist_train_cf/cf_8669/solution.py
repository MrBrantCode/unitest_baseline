"""
QUESTION:
Write a function named `sum_of_numbers` that takes a list of integers as input and returns the sum of all numbers in the list, excluding those divisible by both 3 and 5. The function should handle non-integer inputs by returning an error message. The function should also sort the list in ascending order before performing calculations if the input list is not already sorted.
"""

def sum_of_numbers(lst):
    try:
        sorted_lst = sorted(lst)
        sum = 0
        for num in sorted_lst:
            if not (num % 3 == 0 and num % 5 == 0):
                sum += num
        return sum
    except TypeError:
        return "Error: Invalid input. All elements of the list must be integers."
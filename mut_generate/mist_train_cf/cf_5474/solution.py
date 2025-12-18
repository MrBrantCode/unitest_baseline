"""
QUESTION:
Write a function called `find_second_highest` that takes a list of numbers as input and returns the second highest value in the list. The function should not use any built-in sorting or max/min functions, should handle duplicate values and negative numbers, and should run in O(n) time complexity. If the list has less than two elements, the function should return None.
"""

def find_second_highest(my_list):
    if len(my_list) < 2:
        return None

    max_val = my_list[0]
    second_max = float('-inf')

    for num in my_list:
        if num > max_val:
            second_max = max_val
            max_val = num
        elif num > second_max and num < max_val:
            second_max = num

    return second_max
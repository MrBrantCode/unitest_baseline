"""
QUESTION:
Write a function `flatten_divisible_by_two_and_three` that takes a list of lists as input and returns a flattened list containing only the integers that are divisible by both 2 and 3.
"""

def flatten_divisible_by_two_and_three(lst):
    flattened_list = []
    for sublist in lst:
        for num in sublist:
            if num % 2 == 0 and num % 3 == 0:
                flattened_list.append(num)
    return flattened_list
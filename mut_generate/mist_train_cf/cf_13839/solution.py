"""
QUESTION:
Implement a function named `sort_list` that takes a list of integers as input and returns a tuple containing the sorted list in ascending order and the number of swaps performed during the sorting process. The function should handle duplicate integers in the input list, use only constant space, and not use any built-in sorting functions.
"""

def sort_list(input_list):
    swaps = 0
    n = len(input_list)
    sorted = False

    while not sorted:
        sorted = True
        for i in range(n-1):
            if input_list[i] > input_list[i+1]:
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
                swaps += 1
                sorted = False

    return (input_list, swaps)
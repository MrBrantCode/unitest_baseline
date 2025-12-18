"""
QUESTION:
Implement a function named `sort_list` that sorts a list of integers in ascending order without using any built-in sorting functions. The function should use constant space and handle duplicate integers. The function should also return the number of swaps performed during the sorting process.
"""

def sort_list(list):
    swaps = 0
    n = len(list)
    sorted = False

    while not sorted:
        sorted = True
        for i in range(n-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                swaps += 1
                sorted = False

    return list, swaps
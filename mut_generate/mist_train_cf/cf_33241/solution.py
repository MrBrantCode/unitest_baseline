"""
QUESTION:
Implement a function `mysteryAlgorithm` that takes a list of integers as input. The function should iterate through the list, swapping adjacent elements if the first element is greater than the second, and continue this process until no more swaps can be made. Return the modified list.
"""

def mysteryAlgorithm(lst):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                sorted = False
    return lst
"""
QUESTION:
Create a function `get_positive_and_sort` that takes a list of integers as input, filters out the positive numbers, sorts them in ascending order without using the built-in `sort()` and `sorted()` functions, and returns the result. Implement a helper function `swap_elements` within `get_positive_and_sort` to swap elements in the list. The `swap_elements` function should take a list and two indices as arguments.
"""

def get_positive_and_sort(l: list):
    def swap_elements(n: list, index1: int, index2: int):
        n[index1], n[index2] = n[index2], n[index1]

    positives = []
    for num in l:
        if num > 0:
            positives.append(num)

    for i in range(len(positives)):
        for j in range(len(positives) - 1):
            if positives[j] > positives[j + 1]:
                swap_elements(positives, j, j + 1)

    return positives
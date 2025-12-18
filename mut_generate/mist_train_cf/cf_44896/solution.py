"""
QUESTION:
Write a function named `cocktail_shaker_sort` that sorts a given list of integers in ascending order using the cocktail shaker sort method. The function should take one argument, a list of integers, and return the sorted list. The list can contain any number of elements, but it must contain at least two elements. The function should not use any built-in sorting methods.
"""

def cocktail_shaker_sort(lst):
    up = range(len(lst) - 1)
    while True:
        for indices in (up, reversed(up)):
            swapped = False
            for i in indices:
                if lst[i] > lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    swapped = True
            if not swapped:
                return lst
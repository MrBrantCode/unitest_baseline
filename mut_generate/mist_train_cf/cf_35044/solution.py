"""
QUESTION:
Implement the `quicksort` function that takes a list of integers as input and returns the sorted list using the Quick Sort algorithm with recursion. The function should sort the list in ascending order. The input list can contain duplicate elements.
"""

def quicksort(xs):
    if len(xs) <= 1:
        return xs
    else:
        pivot = xs[0]
        xs = xs[1:]
        left = [x for x in xs if x <= pivot]
        right = [x for x in xs if x > pivot]

        return quicksort(left) + [pivot] + quicksort(right)
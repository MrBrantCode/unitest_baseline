"""
QUESTION:
Write a function named `find_min_max_indices` that takes a list of integers as input and returns the minimum value, its indices, the maximum value, and its indices. The function should handle duplicate values in the list, have a time complexity of O(n), and a space complexity of O(n).
"""

def find_min_max_indices(lst):
    if not lst:
        return []

    min_value = max_value = lst[0]
    min_indices = [0]
    max_indices = [0]

    for i in range(1, len(lst)):
        if lst[i] < min_value:
            min_value = lst[i]
            min_indices = [i]
        elif lst[i] == min_value:
            min_indices.append(i)
        elif lst[i] > max_value:
            max_value = lst[i]
            max_indices = [i]
        elif lst[i] == max_value:
            max_indices.append(i)

    return min_value, min_indices, max_value, max_indices
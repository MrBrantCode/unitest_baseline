"""
QUESTION:
Write a function called `find_min_max` that takes a list of numbers as input and returns the minimum and maximum numbers along with their corresponding indices. The function should not use any built-in functions or methods for finding the minimum and maximum, and it should have a time complexity of O(n), where n is the length of the list. The function should also handle the case where the list contains duplicates by returning the indices of all occurrences of the minimum and maximum elements in the original list.
"""

def find_min_max(lst):
    min_num = lst[0]
    max_num = lst[0]
    min_indices = [0]
    max_indices = [0]

    for i in range(1, len(lst)):
        if lst[i] < min_num:
            min_num = lst[i]
            min_indices = [i]
        elif lst[i] == min_num:
            min_indices.append(i)
        elif lst[i] > max_num:
            max_num = lst[i]
            max_indices = [i]
        elif lst[i] == max_num:
            max_indices.append(i)

    return min_num, min_indices, max_num, max_indices
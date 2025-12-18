"""
QUESTION:
Write a function `sort_list` that takes a list of numbers as input and returns a new list with the numbers sorted in ascending order. The function should not use any built-in sorting functions or methods. The list can contain any number of elements and the elements can be any integer.
"""

def sort_list(n_list):
    for i in range(len(n_list)):
        min_idx = i
        for j in range(i+1, len(n_list)):
            if n_list[j] < n_list[min_idx]:
                min_idx = j
        n_list[i], n_list[min_idx] = n_list[min_idx], n_list[i]
    return n_list
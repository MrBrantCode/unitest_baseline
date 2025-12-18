"""
QUESTION:
Write a function named `selection_sort` that implements the selection sort algorithm to sort a list of numbers in ascending order. The function should take a list of integers as input and return the sorted list. The function should not use any built-in sorting functions.
"""

def selection_sort(input_list):
    for idx in range(len(input_list)):
        min_idx = idx
        for j in range(idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]
            
    return input_list
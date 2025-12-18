"""
QUESTION:
Implement a function named `find_even_indexes` that takes a list of integers as input. The function should return a list of elements at even indexes in the input list, excluding any negative numbers, and sorted in descending order. The input list is not empty and contains only integers.
"""

def find_even_indexes(lst):
    even_indexes = []
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] >= 0:
            even_indexes.append(lst[i])
    return sorted(even_indexes, reverse=True)
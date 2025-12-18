"""
QUESTION:
Implement a function named `selection_sort` that sorts a list of numbers in non-decreasing order using the selection sort algorithm. The function should take a list of integers as input and return the sorted list. The function should modify the original list by repeatedly finding the minimum element from the unsorted part and swapping it with the first unsorted element.
"""

def selection_sort(list): 
    for i in range(len(list)): 
        min_idx = i 
        for j in range(i+1, len(list)): 
            if list[min_idx] > list[j]: 
                min_idx = j 
        list[i], list[min_idx] = list[min_idx], list[i]
    return list
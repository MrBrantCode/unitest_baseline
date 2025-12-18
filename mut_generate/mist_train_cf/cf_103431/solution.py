"""
QUESTION:
Implement a function `sort_list(self, lst)` in a class that sorts a list of numbers in ascending order using the bubble sort algorithm. The function should take a list of integers as input and return the sorted list. The function must use a nested loop structure, where the outer loop iterates over each element in the list, and the inner loop compares each pair of adjacent elements and swaps them if they are in the wrong order. The input list is modified in-place.
"""

def sort_list(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
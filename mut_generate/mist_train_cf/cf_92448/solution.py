"""
QUESTION:
Create a function named `binary_search` that takes a sorted list of integers `lst` and a target integer `target` as parameters. The function should return the index of the target integer in the list if found, and -1 otherwise. The list is sorted in ascending order.
"""

def binary_search(lst, target):
    start = 0
    end = len(lst) - 1
    
    while start <= end:
        middle = (start + end) // 2
        if lst[middle] == target:
            return middle
        elif lst[middle] > target:
            end = middle - 1
        else:
            start = middle + 1
    
    return -1
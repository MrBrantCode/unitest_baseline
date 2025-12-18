"""
QUESTION:
Create a function named `binary_search` that takes two parameters: a sorted list of integers and a target integer. The function should return the index of the target integer in the list if it is found, and -1 if it is not found. The list and target integer will always be provided, and the list will be sorted in ascending order.
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
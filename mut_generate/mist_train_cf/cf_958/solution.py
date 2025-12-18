"""
QUESTION:
Create a function called "search_value" that takes a sorted list and a value as input and returns true if the value is present in the list, otherwise false. The function should use a binary search algorithm to find the value in the list. The input list will be sorted in ascending order and will have a maximum length of 1000 elements.
"""

def search_value(lst, val):
    start = 0
    end = len(lst) - 1
    
    while start <= end:
        middle = (start + end) // 2
        
        if lst[middle] == val:
            return True
        elif lst[middle] > val:
            end = middle - 1
        else:
            start = middle + 1
    
    return False
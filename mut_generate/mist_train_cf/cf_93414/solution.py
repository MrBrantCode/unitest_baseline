"""
QUESTION:
Implement a function called `binary_search` that takes two parameters: a sorted list `arr` and a target value `target`. The function should return `True` if the `target` is found in the list and `False` otherwise. The function should have a time complexity of O(log n). If the list contains only one item, it should return whether the item matches the target.
"""

def binary_search(arr, target):
    if len(arr) == 1:
        return arr[0] == target
    
    if len(arr) == 0:
        return False
    
    mid = len(arr) // 2
    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return binary_search(arr[mid+1:], target)
    else:
        return binary_search(arr[:mid], target)
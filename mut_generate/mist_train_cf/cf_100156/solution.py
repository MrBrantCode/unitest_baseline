"""
QUESTION:
Create a function named `three_sum` that takes a list of integers `lst` and a target sum `target_sum` as input. The function should return `True` if there exist three distinct integers in the list whose sum is equal to the target sum, and `False` otherwise. The function must only consider lists that contain at least three distinct positive integers and a positive target sum.
"""

def three_sum(lst, target_sum):
    # Check if list contains only positive integers
    if not all(num > 0 for num in lst):
        return False
    
    # Check if target sum is positive
    if target_sum <= 0:
        return False
    
    # Check if list contains duplicates
    if len(lst) != len(set(lst)):
        return False
    
    lst.sort()
    n = len(lst)
    for i in range(n-2):
        left, right = i+1, n-1
        while left < right:
            if lst[i] + lst[left] + lst[right] == target_sum:
                return True
            elif lst[i] + lst[left] + lst[right] < target_sum:
                left += 1
            else:
                right -= 1
    return False
"""
QUESTION:
Write a function `three_sum(lst, target_sum)` that takes a list of integers `lst` and a target sum `target_sum` as input. The function should return `True` if there exist three integers in the list whose sum is equal to the target sum and `False` otherwise. The list must contain only positive integers, the target sum must be positive, the list must not contain duplicates, and the list must have at least three integers.
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
    
    # Check if list has at least three integers
    if len(lst) < 3:
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
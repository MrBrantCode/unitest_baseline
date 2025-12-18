"""
QUESTION:
Design a function `check_exists(lst1, lst2)` that takes two lists of integers `lst1` and `lst2` as input. The function should return `True` if `lst1` contains at least one element from `lst2` or if two elements in `lst1` can be combined to form at least one number from `lst2`, and `False` otherwise. The function should be efficient enough to handle large size lists.
"""

def check_exists(lst1, lst2):
    lst1.sort()
    for num in lst2:
        left = 0
        right = len(lst1) - 1
        while left < right:
            if lst1[left] + lst1[right] == num:
                return True
            elif lst1[left] + lst1[right] < num:
                left += 1
            else:
                right -= 1
    return False
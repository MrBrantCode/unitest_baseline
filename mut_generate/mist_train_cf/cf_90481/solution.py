"""
QUESTION:
Write a function `is_sorted(lst)` that checks if a given list of integers is sorted in ascending order and contains no duplicate values. The function should not use any built-in sorting functions, and it should have a time complexity less than O(n^2) and a space complexity less than O(n). The length of the list is between 1 and 10^6, and the values in the list are between -10^9 and 10^9.
"""

def is_sorted(lst):
    if len(lst) <= 1:
        return True
    if len(lst) != len(set(lst)):
        return False
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    return True
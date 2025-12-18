"""
QUESTION:
Write a function named `is_sorted` that checks if a given list of integers is sorted in ascending order and contains no duplicate values. The function should not use any built-in sorting functions and should handle edge cases efficiently. The time complexity of the function should be less than O(n^2) and the space complexity should be less than O(n). The length of the list is between 1 and 10^6, and the values in the list are between -10^9 and 10^9.
"""

def is_sorted(lst):
    # Check if the list is empty or has only one element
    if len(lst) <= 1:
        return True
    
    # Check if the list contains any duplicates
    if len(lst) != len(set(lst)):
        return False
    
    # Check if the list is sorted in ascending order
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    
    return True
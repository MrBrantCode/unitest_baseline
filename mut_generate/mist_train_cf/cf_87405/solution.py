"""
QUESTION:
Implement the `merge_sort_iterative` function to sort a list of numbers in descending order using the iterative merge sort algorithm. The function should not use any built-in sorting functions or libraries. The input list may contain duplicate numbers and will always have at least one element. Return the sorted list.
"""

def merge_sort_iterative(lst):
    if len(lst) <= 1:
        return lst
    
    width = 1
    while width < len(lst):
        left = 0
        while left < len(lst):
            right = min(left + (2 * width), len(lst))
            mid = left + width
            left_half = lst[left:mid]
            right_half = lst[mid:right]
            
            lst[left:right] = sorted(left_half + right_half, reverse=True)
            
            left += 2 * width
        width *= 2
    return lst
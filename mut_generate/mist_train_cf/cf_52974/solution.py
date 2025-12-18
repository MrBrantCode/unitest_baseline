"""
QUESTION:
Implement a function `median` that takes a list `l` as input and returns the median of its elements. The function should not use any built-in functions for list sorting or median calculation and should not modify the original list order. The function should handle lists of various lengths, including both even and odd numbers of elements.
"""

def median(lst):
    """
    This function calculates the median of a list without using built-in functions for sorting or median calculation.
    
    Args:
    lst (list): The input list of elements.
    
    Returns:
    float: The median of the input list elements.
    """
    
    # Implement the merge sort algorithm to sort the input list
    def merge_sort(lst):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left_half = merge_sort(lst[:mid])
        right_half = merge_sort(lst[mid:])
        res = []
        while left_half and right_half:
            if left_half[0] < right_half[0]:
                res.append(left_half.pop(0))
            else:
                res.append(right_half.pop(0))
        res.extend(left_half if left_half else right_half)
        return res

    # Sort the input list using the merge sort function
    lst_sorted = merge_sort(lst)
    
    # Calculate the median according to the length of the sorted list
    len_lst = len(lst_sorted)
    if len_lst % 2 == 1:
        return lst_sorted[len_lst // 2]
    return (lst_sorted[len_lst // 2 - 1] + lst_sorted[len_lst // 2]) / 2
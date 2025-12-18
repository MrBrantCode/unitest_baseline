"""
QUESTION:
Write a function called `find_median` that takes a list of integers as input and returns the median of the list. If the list is empty, return None. If the list has an odd number of elements, return the middle element. If the list has an even number of elements, return the average of the two middle elements. The function should handle lists with any number of elements and should not modify the input list.
"""

def find_median(lst):
    # Step 1
    if len(lst) == 0:
        return None

    # Step 2
    sorted_lst = sorted(lst)

    # Step 3
    length = len(sorted_lst)

    # Step 4
    if length % 2 != 0:
        return sorted_lst[length // 2]

    # Step 5
    first_middle = sorted_lst[length // 2 - 1]
    second_middle = sorted_lst[length // 2]
    return (first_middle + second_middle) / 2
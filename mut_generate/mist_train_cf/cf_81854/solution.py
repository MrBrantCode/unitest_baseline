"""
QUESTION:
Write a function `common(l1: list, l2: list)` that takes two lists of integers as input and returns a new list containing the unique integers that are common to both input lists, sorted in ascending order. The function should not use any built-in Python list methods or functions for sorting or removing duplicates, and it should be able to handle negative integers.
"""

def common(l1: list, l2: list) -> list:
    """
    Return a sorted, unique list of common elements between two input lists. 
    No built-in Python list functionality is used. Also handles negative numbers.
    """

    # Function to remove duplicates
    def remove_duplicates(lst: list) -> list:
        result = []
        for i in lst:
            if i not in result:
                result.append(i)
        return result

    # Function to sort list
    def bubble_sort(lst: list) -> list:
        while True:
            was_sorted = False
            for i in range(len(lst)-1):
                if lst[i] > lst[i+1]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]
                    was_sorted = True
            if was_sorted is False:
                return lst
    
    l1_no_duplicates = remove_duplicates(l1)
    l2_no_duplicates = remove_duplicates(l2)

    common_no_duplicates = []
    for i in l1_no_duplicates:
        if i in l2_no_duplicates:
            common_no_duplicates.append(i)
    
    return bubble_sort(common_no_duplicates)
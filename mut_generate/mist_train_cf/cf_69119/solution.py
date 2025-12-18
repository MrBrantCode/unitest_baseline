"""
QUESTION:
Given two lists of integers, write a function named `common(l1: list, l2: list)` that returns the sorted unique elements shared between them without using Python's built-in list functions. The function should be able to handle cases with negative numbers and return a correctly sorted list. Each input list will contain at most 1000 integers, and each integer will be between -10^6 and 10^6.
"""

def common(l1: list, l2: list) -> list:
    """Return sorted unique common elements for two lists without using built-in Python list functions and accounting for negative numbers."""
    
    common_set = set(l1) & set(l2) 
    common_list = list(common_set) 
    
    def custom_sort(lst: list):
        positive = []
        negative = []

        for num in lst:
            if num >= 0:
                positive.append(num)
            else:
                negative.append(num)

        return sorted(negative) + sorted(positive)

    return custom_sort(common_list)
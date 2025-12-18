"""
QUESTION:
Write a function named `find_smallest_non_negative` that takes two lists of floating-point numbers as input. The function should return the smallest non-negative number from each list. If a list does not contain any non-negative numbers, the function should return `None` for that list. The function should handle empty lists and lists containing only negative numbers.
"""

def find_smallest_non_negative(list1, list2):
    min1 = float('inf')
    min2 = float('inf')

    for i in list1:
        if i >= 0 and i < min1:
            min1 = i
            
    for i in list2:
        if i >= 0 and i < min2:
            min2 = i

    return min1 if min1 != float('inf') else None, min2 if min2 != float('inf') else None
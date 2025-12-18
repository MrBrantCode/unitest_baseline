"""
QUESTION:
Create a function `double_and_sort(lst)` that takes a list of integers as input, doubles each element, sorts the resulting list in ascending order without modifying the original list, and returns the sorted list. The function should handle duplicate elements and empty lists, and must implement a custom sorting algorithm without using built-in sorting functions or libraries.
"""

def double_and_sort(lst):
    # Check if the list is empty
    if not lst:
        return []
    
    # Double every element in the list using list comprehension
    doubled_list = [2 * num for num in lst]
    
    # Sort the doubled list using a custom sorting algorithm
    for i in range(len(doubled_list)):
        for j in range(i + 1, len(doubled_list)):
            if doubled_list[i] > doubled_list[j]:
                doubled_list[i], doubled_list[j] = doubled_list[j], doubled_list[i]
    
    return doubled_list
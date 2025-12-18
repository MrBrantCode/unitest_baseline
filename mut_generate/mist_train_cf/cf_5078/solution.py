"""
QUESTION:
Create a function called custom_sort that sorts a list of integers and/or floating-point numbers in descending order. The function should not use any built-in sorting functions or methods, have a time complexity of O(n^2), and not use any additional data structures. The input list can contain duplicate numbers, be empty, have a length up to 100000, and may include negative numbers, positive numbers, and/or floating-point numbers.
"""

def custom_sort(lst):
    length = len(lst)
    
    if length <= 1:
        return lst
    
    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    
    return lst
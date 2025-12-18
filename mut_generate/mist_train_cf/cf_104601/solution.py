"""
QUESTION:
Create a class with a method `sort_list` that sorts a given list of numbers in ascending order using the Bubble Sort algorithm. The `sort_list` method should take a list of numbers as input and return the sorted list. The sorting should be done in-place, meaning it should modify the original list. The input list can contain duplicate numbers and the method should be able to handle it.
"""

def sort_list(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]: 
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
"""
QUESTION:
Create a function named `sort_by_second_element` that sorts a 2-dimensional list in ascending order based on the values of the second element in each sublist. The function should take a 2D list as input, modify the original list, and return the sorted list.
"""

def sort_by_second_element(lst): 
    lst.sort(key = lambda x: x[1]) 
    return lst
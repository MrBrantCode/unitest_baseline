"""
QUESTION:
Create a function named `remove_duplicates` that takes a list containing a mixture of integers and strings as input and returns a new list with duplicate elements removed. Two elements are considered duplicates if they have the same value and the same type.
"""

def remove_duplicates(lst):
    unique_set = set()
    unique_list = []
    
    for element in lst:
        if element not in unique_set:
            unique_set.add(element)
            unique_list.append(element)
            
    return unique_list
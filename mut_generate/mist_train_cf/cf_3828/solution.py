"""
QUESTION:
Write a function called `find_unique_elements` that takes two lists as input and returns a new list consisting of elements which are present in only one of the input lists. The function should not use any built-in Python functions or methods such as `set()` or list comprehension, and its time complexity should be O(n^2), where n is the length of the longer list. Implement the function using only a single loop (no nested loops or recursion) by iterating over the lists sequentially.
"""

def find_unique_elements(list1, list2):
    unique_elements = []
    
    for element in list1 + list2:
        if (element in list1) ^ (element in list2):
            unique_elements.append(element)
    
    return unique_elements
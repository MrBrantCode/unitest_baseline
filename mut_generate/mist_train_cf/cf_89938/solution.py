"""
QUESTION:
Implement a function named `find_unique_elements` that takes a list of integers as input and returns a new list containing the unique elements from the input list in their original order, without using any built-in functions or libraries. The input list can contain negative integers and duplicate values.
"""

def find_unique_elements(lst):
    unique_lst = []
    for num in lst:
        if num not in unique_lst:
            unique_lst.append(num)
    return unique_lst
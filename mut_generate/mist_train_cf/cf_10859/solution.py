"""
QUESTION:
Write a function called `move_element_to_beginning` that takes a list `lst` as input and rearranges its elements by moving the second-to-last element to the beginning. If the list has less than 2 elements, the function should return the original list.
"""

def move_element_to_beginning(lst):
    if len(lst) >= 2:
        second_to_last = lst[-2]
        lst.insert(0, second_to_last)
        lst.pop(-2)
    return lst
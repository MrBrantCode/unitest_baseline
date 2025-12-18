"""
QUESTION:
Write a function called `move_element` that takes a list as input and moves the element at index 0 to the end of the list if it is not already at the end, otherwise move it to the beginning. The function should return the modified list and operate in O(1) time complexity, or explain why this is not possible with the given data structure.
"""

def move_element(lst):
    if len(lst) == 0:
        return lst
    if lst[0] == lst[-1]:
        lst.insert(0, lst.pop())
    else:
        lst.append(lst.pop(0))
    return lst
"""
QUESTION:
Create a function `swap_elements` that takes a list of any length and data type as input. The function should swap the first and last elements, the second and second last elements, the third and third last elements, and so on, effectively reversing the order of the elements in the list without reversing the list itself.
"""

def swap_elements(lst):
    length = len(lst)
    for i in range(length//2):
        lst[i], lst[length-1-i] = lst[length-1-i], lst[i]
    return lst
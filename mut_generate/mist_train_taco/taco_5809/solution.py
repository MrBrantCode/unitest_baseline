"""
QUESTION:
Write a function that takes a list of at least four elements as an argument and returns a list of the middle two or three elements in reverse order.
"""

def get_middle_elements_reversed(lst):
    if len(lst) < 4:
        raise ValueError("The list must contain at least four elements.")
    
    l = len(lst) // 2 - 1
    return lst[l:-l][::-1]
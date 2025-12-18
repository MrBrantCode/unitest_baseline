"""
QUESTION:
Create a function named `sort_4th_dimension` that sorts a 4-dimensional list by the values of the third element in the second sub-sublist of each sub-sublist. The function should be able to handle cases where the third element in the second sub-sublist is another sublist, and it should not alter the original dataset. The list is assumed to be well-structured with at least three elements in the second sub-sublist of every sub-sublist.
"""

def sort_4th_dimension(lst):
    return sorted(lst, key=lambda x: x[1][2] if isinstance(x[1][2], (int,float)) else sum(x[1][2]))
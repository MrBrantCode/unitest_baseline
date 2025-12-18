"""
QUESTION:
Create a function named `find_index_2d` that takes two parameters: a jagged 2D list and an element. The function should return a tuple containing the index of the sub-list and the index of the element within that sub-list if the element exists in the list; otherwise, it should return `None`.
"""

def find_index_2d(my_list, elm): 
    for i, sub_list in enumerate(my_list):
        if elm in sub_list:
            return (i, sub_list.index(elm))
    return None
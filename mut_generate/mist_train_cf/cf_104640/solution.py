"""
QUESTION:
Write a function `delete_element(lst, element)` that takes a list `lst` and an element as input, and returns a tuple containing the modified list and the number of times the element was deleted. The function should delete the first occurrence of the element in the list if it exists, and return the original list if the element is not found. The function should work correctly even if the element is a negative number.
"""

def delete_element(lst, element):
    deletion_count = 0
    if element in lst:
        lst.remove(element)
        deletion_count += 1
    return lst, deletion_count
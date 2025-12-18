"""
QUESTION:
Create a function called `find_intersection` that takes two lists (`list1` and `list2`) of any data type as input and returns a list of elements that are common to both lists. The function should have a time complexity of O(n) and should not use any built-in functions or libraries, except for the creation of a set.
"""

def find_intersection(list1, list2):
    intersecting_elements = []
    set1 = set(list1)
    for element in list2:
        if element in set1:
            intersecting_elements.append(element)
    return intersecting_elements
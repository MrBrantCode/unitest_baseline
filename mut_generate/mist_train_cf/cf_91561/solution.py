"""
QUESTION:
Create a function `find_common_elements(list1, list2)` that takes two lists as arguments and returns a list of elements present in both lists without duplicates, sorted in ascending order.
"""

def find_common_elements(list1, list2):
    common_elements = set()
    for element in list1:
        if element in list2 and element not in common_elements:
            common_elements.add(element)
    return sorted(list(common_elements))
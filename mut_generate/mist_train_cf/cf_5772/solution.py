"""
QUESTION:
Create a function `find_common_elements(list1, list2)` that takes two lists as input and returns their common elements, including duplicates, in sorted order. The function should not use the built-in set() function or any additional data structures, and its time complexity should be O(n^2), where n is the total number of elements in both lists.
"""

def find_common_elements(list1, list2):
    common_elements = []
    for element1 in list1:
        for element2 in list2:
            if element1 == element2:
                common_elements.append(element1)
                list2.remove(element2)
                break
    return sorted(common_elements)
"""
QUESTION:
Create a function `find_common_elements(list1, list2)` that takes two lists as input and returns a new list containing all common elements from both lists. The function should not use the built-in `set()` function or any additional data structures, handle duplicate elements, and return the common elements in sorted order. The time complexity of the function should be O(n^2), where n is the total number of elements in both lists.
"""

def entrance(list1, list2):
    common_elements = []
    for element1 in list1:
        for element2 in list2:
            if element1 == element2:
                common_elements.append(element1)
                list2.remove(element2)
                break
    return sorted(common_elements)
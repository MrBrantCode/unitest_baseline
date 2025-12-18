"""
QUESTION:
Implement a function `find_common_elements(lst1, lst2)` that takes two lists `lst1` and `lst2` as input and returns a new list containing only the elements that appear in both lists. The function should not use any built-in Python functions or libraries, and it should have a time complexity of O(n), where n is the length of the longest input list.
"""

def find_common_elements(lst1, lst2):
    unique_elements = set()
    for elem in lst1:
        unique_elements.add(elem)
    common_elements = []
    for elem in lst2:
        if elem in unique_elements:
            common_elements.append(elem)
    return common_elements
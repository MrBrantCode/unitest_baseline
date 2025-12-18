"""
QUESTION:
Implement a function named `add_element` that adds a unique element to a dynamic set with an average time complexity of O(1) and a space complexity of O(n), where n is the number of elements already in the set. The function should return True if the element is added successfully and False if the element already exists in the set.
"""

def add_element(element, dynamic_set):
    if element not in dynamic_set:
        dynamic_set.add(element)
        return True
    return False
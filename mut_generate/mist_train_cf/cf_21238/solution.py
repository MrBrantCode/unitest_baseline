"""
QUESTION:
Find the maximum and second maximum elements in a linked list, along with their indices. The function `find_max_elements(head)` should take the head of the linked list as input and return the maximum element, second maximum element, index of the maximum element, and index of the second maximum element. Assume the linked list is not empty, and if there are multiple occurrences of the maximum or second maximum elements, return the index of the first occurrence.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def find_max_elements(head):
    max_element = float('-inf')
    second_max_element = float('-inf')
    max_index = -1
    second_max_index = -1
    index = 0

    current = head
    while current is not None:
        if current.data > max_element:
            second_max_element = max_element
            second_max_index = max_index
            max_element = current.data
            max_index = index
        elif current.data > second_max_element and current.data != max_element:
            second_max_element = current.data
            second_max_index = index
        
        current = current.next
        index += 1

    return max_element, second_max_element, max_index, second_max_index
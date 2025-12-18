"""
QUESTION:
Write a function named `searchLinkedList` that searches for the first occurrence of a specific element in a linked list and returns its index. If the element is not found, the function should return -1. The time complexity of the function should be O(n), where n is the number of elements in the linked list. The function should take two parameters: the head of the linked list and the target element to be searched.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def searchLinkedList(head, element):
    """
    Searches for the first occurrence of a specific element in a linked list and returns its index.
    
    Args:
        head (Node): The head of the linked list.
        element: The target element to be searched.
    
    Returns:
        int: The index of the first occurrence of the element if found, -1 otherwise.
    """
    currentNode = head
    index = 0
    while currentNode is not None:
        if currentNode.value == element:
            return index
        currentNode = currentNode.next
        index += 1
    return -1
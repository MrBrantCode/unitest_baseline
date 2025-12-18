"""
QUESTION:
Create a function called `convertToLinkedList` that takes an array as input, converts it into a singly linked list without using a loop (instead use recursion) and in reverse order, and removes all duplicate elements. The function should return the head of the resulting linked list.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def convertToLinkedList(array):
    def insert(root, value, uniqueElements):
        if value not in uniqueElements:
            newNode = Node(value)
            newNode.next = root
            uniqueElements.add(value)
            return newNode
        else:
            return root

    def helper(root, array, index, uniqueElements):
        if index == len(array):
            return root
        root = insert(root, array[index], uniqueElements)
        return helper(root, array, index + 1, uniqueElements)

    return helper(None, array, 0, set())
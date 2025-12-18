"""
QUESTION:
Create a function called `convertToLinkedList` that takes a list of integers as input and returns the head node of a singly linked list. The linked list should contain the unique elements of the input list in reverse order. The function should not use a loop to construct the linked list. Instead, it should use recursive calls or a functional approach to achieve this.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def insert(root, value):
    newNode = Node(value)
    newNode.next = root
    root = newNode
    return root

def convertToLinkedList(array):
    def recursive_convert(array, uniqueElements, linkedList):
        if not array:
            return linkedList
        if array[0] not in uniqueElements:
            linkedList = insert(linkedList, array[0])
            uniqueElements.add(array[0])
        return recursive_convert(array[1:], uniqueElements, linkedList)

    linkedList = None
    uniqueElements = set()
    return recursive_convert(array, uniqueElements, linkedList)
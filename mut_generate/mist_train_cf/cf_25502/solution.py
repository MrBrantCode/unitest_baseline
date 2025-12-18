"""
QUESTION:
Create a function `convertToLinkedList(arr)` that takes an array of integers as input and returns the head of a singly linked list representing the input array, without using an explicit loop. The function should utilize recursive calls to achieve this transformation.
"""

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

def convertToLinkedList(arr):
    if not arr:
        return None

    # Recursive case: Create a new node with the first element of the array
    # and recursively convert the rest of the array to a linked list
    node = Node(arr[0])
    node.next = convertToLinkedList(arr[1:])
    
    return node
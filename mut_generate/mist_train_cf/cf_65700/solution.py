"""
QUESTION:
Write a function `swapNodes(x, y)` that swaps two distinct nodes with values `x` and `y` in a singly linked list, assuming that the values of the nodes are known. The function should work for any positions of `x` and `y` in the list, including the head and tail, and should handle the case where `x` and `y` are the same or not present in the list.
"""

class Node: 
    def __init__(self, data = None, next = None): 
        self.data = data 
        self.next = next

def swapNodes(head, x, y):
    if x == y: 
        return head

    prevX = None
    currX = head 
    while currX != None and currX.data != x: 
        prevX = currX 
        currX = currX.next

    prevY = None
    currY = head 
    while currY != None and currY.data != y: 
        prevY = currY 
        currY = currY.next

    if currX == None or currY == None: 
        return head

    if prevX != None: 
        prevX.next = currY 
    else: 
        head = currY 

    if prevY != None: 
        prevY.next = currX 
    else: 
        head = currX 

    temp = currX.next
    currX.next = currY.next
    currY.next = temp 

    return head
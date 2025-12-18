"""
QUESTION:
Implement a function `getIndices(arr, num)` that takes an array `arr` and an integer `num` as input. The function should return a linked list containing the indices of all occurrences of `num` in `arr`. If `num` is not found in `arr`, return `-1`. The function should handle duplicate occurrences of `num` in `arr` and return their indices in the linked list.
"""

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(None)
        
    def insert(self, x):
        if(self.head.val is None):
            self.head = Node(x)
        else:
            cur = self.head
            while(cur.next):
                cur = cur.next
            cur.next = Node(x)

def getIndices(arr, num):
    ll = LinkedList()
    for i in range(len(arr)):
        if arr[i] == num:
            ll.insert(i)
    if(ll.head.val is None):
        return -1
    return ll
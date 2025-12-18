"""
QUESTION:
Implement a function `set_intersection` that finds the intersection of two linked lists, `s1` and `s2`, with an optional parameter `remove` to exclude a specific value from the intersection. The function should return a sorted list of the intersection elements. 

The `set_intersection` function should take three parameters: `s1` and `s2` as instances of the `LinkedList` class, and `remove` as an optional integer value. The `LinkedList` class should have an `append` method to add elements to the list and a `head` attribute to access the first node of the list. The `Node` class should have `data` and `next` attributes to store the node's value and the reference to the next node, respectively.
"""

from typing import Optional

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

def set_intersection(s1, s2, remove: Optional[int] = None):
    map1 = {}
    map2 = {}

    node = s1.head
    while node:
        if node.data != remove:
            map1[node.data] = True
        node = node.next

    node = s2.head
    while node:
        if node.data != remove and node.data in map1 and node.data not in map2:
            map2[node.data] = node.data
        node = node.next

    return sorted(list(map2.values()))
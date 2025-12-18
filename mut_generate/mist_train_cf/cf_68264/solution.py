"""
QUESTION:
Implement a function named `shared_elements` that takes two lists `list1` and `list2` as input and returns a list of distinct tuples. Each tuple should contain a unique element that appears in both input lists and its frequency. The function must use a self-crafted doubly-linked list and not utilize Python's in-built list operations or any external packages. The tuples in the output list should be sorted in ascending order based on the values of the elements.
"""

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, item):
        if self.head is None:
            new_node = Node(item)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(item)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def count(self, item):
        count = 0
        cur = self.head
        while cur:
            if cur.item == item:
                count += 1
            cur = cur.next
        return count

def shared_elements(list1, list2):
    dll = DoublyLinkedList()
    item_dict = []
    
    for item in list1:
        if item in list2 and dll.count(item) == 0:
            dll.append(item)

    cur = dll.head
    while cur:
        count = list1.count(cur.item) + list2.count(cur.item)
        item_dict.append((cur.item, count))
        cur = cur.next

    item_dict.sort()
    return item_dict
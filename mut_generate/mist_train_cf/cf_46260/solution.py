"""
QUESTION:
Write a method called `get_intersection` to find the intersection of two sorted linked lists. Each node in the linked list has an integer value. The method should return the intersection as a linked list. The linked lists may have duplicate elements, but the returned intersection should only contain unique elements.
"""

class Node:
    def __init__(self, data):
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

def get_intersection(list1, list2):
    cur1 = list1.head
    cur2 = list2.head
    result = LinkedList()
    seen = set()
    while cur1 and cur2:
        if cur1.data == cur2.data and cur1.data not in seen:
            result.append(cur1.data)
            seen.add(cur1.data)
            cur1 = cur1.next
            cur2 = cur2.next
        elif cur1.data < cur2.data:
            cur1 = cur1.next
        else:
            cur2 = cur2.next
    return result
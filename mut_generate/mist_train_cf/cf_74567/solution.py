"""
QUESTION:
Merge all the given k sorted linked lists into one sorted linked list and return it. Each linked list is represented by a ListNode and is sorted in non-decreasing order. The number of nodes in all the linked-lists is in the range [0, 5000] and the value of each node is in the range [-10^6, 10^6]. The function name should be `mergeKLists` and it should take a list of linked lists as input.
"""

from queue import PriorityQueue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Wrapper:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val

def mergeKLists(lists):
    head = point = ListNode(0)
    q = PriorityQueue()

    for l in lists:
        if l:
            q.put(Wrapper(l))

    while not q.empty():
        node = q.get().node
        point.next = node
        point = point.next
        node = node.next
        if node:
            q.put(Wrapper(node))
    return head.next
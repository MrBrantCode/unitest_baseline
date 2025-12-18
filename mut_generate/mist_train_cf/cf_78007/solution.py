"""
QUESTION:
Implement a function `merge_sort` that sorts a linked list in ascending order using the merge sort algorithm. The function should take the head of the linked list as input and return the head of the sorted linked list. Assume the linked list node class is `Node` with `data` and `next` attributes. The input linked list may be empty or contain one or more nodes.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_merge(a, b):
    result = None

    if a is None:
        return b
    if b is None:
        return a

    if a.data <= b.data:
        result = a
        result.next = sorted_merge(a.next, b)
    else:
        result = b
        result.next = sorted_merge(a, b.next)
    return result

def get_middle(head):
    if head is None:
        return head

    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge_sort(head):
    if head is None or head.next is None:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next

    middle.next = None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    sorted_list = sorted_merge(left, right)
    return sorted_list
"""
QUESTION:
Write a function `merge_sort(head)` that sorts a doubly linked list in ascending order. The function should take the head of the doubly linked list as input and return the head of the sorted doubly linked list. The time complexity of the function should be no worse than O(n log n), and the function should not convert the doubly linked list to a list/array or any other data structure.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def split(head):
    fast = slow =  head
    while(True):
        if fast.next is None:
            break
        if fast.next.next is None:
            break
        fast = fast.next.next
        slow = slow.next
    temp = slow.next
    slow.next = None
    return temp

def merge(first, second): 
    if first is None:
        return second 
    if second is None:
        return first
    if first.data < second.data:
        first.next = merge(first.next, second)
        first.next.prev = first
        first.prev = None  
        return first
    else:
        second.next = merge(first, second.next)
        second.next.prev = second
        second.prev = None
        return second

def merge_sort(head):
    if head is None:
        return head
    if head.next is None:
        return head
    second = split(head)
    return merge(merge_sort(head), merge_sort(second))
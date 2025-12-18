"""
QUESTION:
Write a function `reverse_list` that takes the head of a singly linked list as input and returns the head of the reversed linked list. Then write a function `find_middle` that takes the head of a singly linked list as input and returns the middle node of the list. If the list has an even number of nodes, return the first middle node. The functions should work in place for the reverse operation and should only make one pass through the list for the find middle operation.
"""

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current is not None:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev

def findMiddle(head: ListNode) -> ListNode:
    slow_ptr = head
    fast_ptr = head
    while fast_ptr is not None and fast_ptr.next is not None:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next
    return slow_ptr
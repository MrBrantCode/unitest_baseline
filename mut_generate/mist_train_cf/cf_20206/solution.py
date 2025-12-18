"""
QUESTION:
Create a function `sortLinkedList` that sorts a singly linked list in descending order. The function should use only constant extra space and return the sorted linked list. The input is the head of the linked list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortLinkedList(head):
    # Reverse the linked list
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    head = prev

    # Bubble sort
    i = head
    while i and i.next:
        j = i
        while j.next:
            if i.val < j.next.val:
                i_val = i.val
                i.val = j.next.val
                j.next.val = i_val
            j = j.next
        i = i.next
    return head
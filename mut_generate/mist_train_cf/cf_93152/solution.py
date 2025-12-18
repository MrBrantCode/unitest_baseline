"""
QUESTION:
Write a function `delete_every_third_element(head)` that takes the head of a linked list as input and returns the head of the modified linked list where every third element is deleted and the remaining elements are in ascending order.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_every_third_element(head):
    if not head:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    current = head
    count = 1

    while current:
        if count % 3 == 0:
            prev.next = current.next
            current = current.next
        else:
            prev = current
            current = current.next

        count += 1

    return dummy.next
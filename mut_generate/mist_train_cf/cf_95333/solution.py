"""
QUESTION:
Write a function `find_middle_element` that takes the head of a linked list as input and returns the value of the middle element if the length of the linked list is odd, and the second middle element if the length is even. The function should traverse the linked list only once.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_middle_element(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.val
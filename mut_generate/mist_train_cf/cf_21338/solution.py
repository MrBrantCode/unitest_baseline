"""
QUESTION:
Write a function `get_second_to_last_element` that takes the head of a singly linked list as input and returns the value of the second-to-last element. The linked list is sorted in ascending order and contains both positive and negative integers. The function should handle cases where the linked list has less than two elements, in which case it should return `None`.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_second_to_last_element(head):
    if not head or not head.next:
        return None
    
    prev = None
    curr = head
    
    while curr.next:
        prev = curr
        curr = curr.next
        
    return prev.val
"""
QUESTION:
Write a function `get_second_to_last_element(head)` that takes the head of a singly linked list as input, where the list is sorted in ascending order and contains both positive and negative integers. The function should return the value of the second-to-last element in the list. If the list has less than two elements, the function should return `None`.
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
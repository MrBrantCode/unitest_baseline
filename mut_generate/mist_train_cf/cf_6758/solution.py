"""
QUESTION:
Write a function `get_second_to_last` that takes the head of a singly linked list as input, where the list is sorted in ascending order, contains both positive and negative integers, and has no duplicate elements. The function should return the value of the second-to-last element in the list. The time complexity of the solution should be O(n) and the space complexity should be O(1).
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_second_to_last(head):
    if head is None or head.next is None:
        return None
    
    slow = head
    fast = head.next
    
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    
    return slow.val
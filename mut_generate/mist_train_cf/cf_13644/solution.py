"""
QUESTION:
Write a function called `mergeLists` that takes two sorted linked lists, `l1` and `l2`, as input and returns the head of a new sorted linked list that contains all the elements from `l1` and `l2`. The function should use recursion to merge the lists. The input linked lists are sorted in ascending order. If one of the input lists is empty, the function should return the other list.
"""

def mergeLists(l1, l2):
    # Base case: if either list is empty, return the other list
    if not l1:
        return l2
    if not l2:
        return l1
    
    # Compare the values of the heads of the two lists
    if l1.val <= l2.val:
        merged = ListNode(l1.val)
        merged.next = mergeLists(l1.next, l2)
    else:
        merged = ListNode(l2.val)
        merged.next = mergeLists(l1, l2.next)
    
    return merged

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
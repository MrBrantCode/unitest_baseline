"""
QUESTION:
Write a function `linked_list_to_array` that takes the head of a singly linked list as input and returns a sorted array in descending order. The function should traverse the linked list, extract its values, and sort them in descending order. The input linked list is a singly linked list where each node has a value and a reference to the next node.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linked_list_to_array(head):
    array = []
    curr = head
    while curr:
        array.append(curr.val)
        curr = curr.next
    array.sort(reverse=True)
    return array
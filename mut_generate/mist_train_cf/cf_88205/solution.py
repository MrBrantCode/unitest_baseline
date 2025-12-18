"""
QUESTION:
Design an algorithm to reverse a singly linked list and sort the reversed list in ascending order based on a string attribute value representing a date in the format "YYYY-MM-DD". The algorithm should handle linked lists with up to 10^6 nodes efficiently, with a time complexity of O(n/2) for reversing and a total time complexity of O(n log n), and use constant extra space if possible. 

Implement two functions: `reverse_linked_list(head)` to reverse the linked list and `sort_linked_list(head)` to sort the reversed linked list. The Node class is defined as `class Node: def __init__(self, date): self.date = date; self.next = None`.
"""

class Node:
    def __init__(self, date):
        self.date = date
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    head = prev
    return head

def sort_linked_list(head):
    if not head or not head.next:
        return head

    mid = get_mid(head)
    next_to_mid = mid.next
    mid.next = None

    left = sort_linked_list(head)
    right = sort_linked_list(next_to_mid)

    return merge_sorted_lists(left, right)

def get_mid(head):
    if not head:
        return head

    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge_sorted_lists(left, right):
    if not left:
        return right
    if not right:
        return left

    if left.date <= right.date:
        result = left
        result.next = merge_sorted_lists(left.next, right)
    else:
        result = right
        result.next = merge_sorted_lists(left, right.next)

    return result
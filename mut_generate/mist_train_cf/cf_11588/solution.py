"""
QUESTION:
Write a function `remove_duplicates` that takes the head of a linked list as input, removes duplicate nodes while preserving the original order of elements, and returns the head of the updated linked list. The function should achieve a time complexity of O(n) and a space complexity of O(n), where n is the number of elements in the linked list.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if not head:
        return head

    seen = set()
    current = head
    seen.add(current.data)

    while current.next:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next

    return head
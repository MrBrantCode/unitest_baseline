"""
QUESTION:
Write a function `get_linked_list_length` that takes in the head node of a linked list and returns the length of the linked list. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the linked list. You are not allowed to modify the original linked list.
"""

def get_linked_list_length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count
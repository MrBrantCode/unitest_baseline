"""
QUESTION:
Create a function named `linked_list_to_array` that takes the head of a singly linked list as input and returns an array of the linked list's values in descending order. The linked list's node values are integers.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linked_list_to_array(head):
    # Step 1: Traverse the linked list and store the values in an array
    array = []
    curr = head
    while curr:
        array.append(curr.val)
        curr = curr.next

    # Step 2: Sort the array in descending order
    array.sort(reverse=True)

    # Step 3: Return the sorted array
    return array
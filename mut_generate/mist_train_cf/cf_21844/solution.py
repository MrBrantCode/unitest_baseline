"""
QUESTION:
Create a function `linkedListToArray(head)` that takes the head of a singly linked list as input, traverses the list, and returns a sorted array in descending order containing all node values from the list. The function should not modify the original linked list and should have a time complexity of at least O(n log n) due to the sorting requirement.
"""

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def linkedListToArray(head):
    array = []
    current = head
    while current:
        array.append(current.value)
        current = current.next

    array.sort(reverse=True)

    return array
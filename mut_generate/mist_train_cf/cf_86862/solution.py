"""
QUESTION:
Implement a function named `remove_greater_elements` that takes the head of a singly linked list of integers as input and returns the head of the updated linked list. The function should remove all elements from the linked list that have a value greater than the sum of all the previous elements. If the linked list is empty or the sum of all the previous elements is equal to or greater than the maximum value in the linked list, the function should return an empty linked list. The algorithm should have a time complexity of O(n), where n is the number of nodes in the linked list, and should not use any additional data structures.
"""

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def remove_greater_elements(head):
    # Step 1: Calculate the sum of all previous elements
    sum = 0
    maxValue = float('-inf')
    node = head
    while node:
        sum += node.value
        maxValue = max(maxValue, node.value)
        node = node.next
    
    # Step 4: Check if the linked list is empty or sum >= maxValue
    if not head or sum >= maxValue:
        return None

    # Step 5: Remove elements with values greater than the sum
    prev = None
    node = head
    while node:
        if node.value > sum:
            if prev:
                prev.next = node.next
            else:
                head = node.next
        else:
            prev = node
        node = node.next

    return head
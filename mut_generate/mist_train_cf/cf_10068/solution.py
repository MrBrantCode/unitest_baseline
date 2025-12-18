"""
QUESTION:
Implement the bubble sort algorithm for a linked list without using any additional data structures or modifying the original linked list. The function, `bubble_sort_linked_list(head)`, should take the head of the linked list as input and return the head of the sorted linked list. The algorithm should have a time complexity of O(n^2), where n is the length of the linked list, and only swap the values of the nodes to achieve sorting.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def bubble_sort_linked_list(head):
    if not head:
        return head
    
    swapped = True
    while swapped:
        swapped = False
        current = head
        prev = None
        
        while current.next:
            if current.data > current.next.data:
                current.data, current.next.data = current.next.data, current.data
                swapped = True
            prev = current
            current = current.next
        
        last = prev
        
    return head
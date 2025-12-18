"""
QUESTION:
Implement a function named `bubble_sort_linked_list` that sorts a linked list in ascending order using the bubble sort algorithm. The function should only swap the values of the nodes without using any additional data structures or modifying the original linked list. The time complexity of the function should be O(n^2), where n is the length of the linked list. The function should take the head of the linked list as input and return the head of the sorted linked list.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def bubble_sort_linked_list(head):
    if not head:
        return head
    
    swapped = True
    last = None
    while swapped:
        swapped = False
        current = head
        
        while current and current.next:
            if current.data > current.next.data:
                current.data, current.next.data = current.next.data, current.data
                swapped = True
            current = current.next
        
        last = current
        
    return head
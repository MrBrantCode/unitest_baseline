"""
QUESTION:
Implement a function named `radix_sort_linked_list` that sorts a singly linked list in ascending order using the Radix sort algorithm. The function should take the head of the linked list as input and return the sorted linked list. The linked list nodes should be sorted based on their integer data values.
"""

def radix_sort_linked_list(head):
    if not head or not head.next:
        return head
    
    # Find the maximum element to determine the number of digits
    max_val = -float('inf')
    current = head
    while current:
        max_val = max(max_val, current.data)
        current = current.next
    
    # Perform Radix sort for each digit position
    exp = 1
    while max_val // exp > 0:
        head = radix_sort_by_digit(head, exp)
        exp *= 10
    
    return head

def radix_sort_by_digit(head, exp):
    bucket = [None] * 10  # Create 10 buckets (0 to 9)
    current = head
    while current:
        # Get the digit value at the current position
        digit = (current.data // exp) % 10
        
        # Insert the node into the corresponding bucket
        if not bucket[digit]:
            bucket[digit] = Node(current.data)
        else:
            node = bucket[digit]
            while node.next:
                node = node.next
            node.next = Node(current.data)
        
        current = current.next
    
    # Merge all the buckets into a new linked list
    new_head = None
    current = None
    for i in range(10):
        if bucket[i]:
            if not new_head:
                new_head = bucket[i]
                current = bucket[i]
            else:
                current.next = bucket[i]
                current = current.next
            # set next to None for the last node in the bucket list
            while current.next:
                current = current.next
            current.next = None
    
    return new_head

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
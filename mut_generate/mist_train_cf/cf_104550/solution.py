"""
QUESTION:
Create a function called `calculate_length_and_sum` that takes the head of a doubly linked list as input. The function should return a tuple containing the total number of nodes in the list and the sum of all node values. If the list is empty (i.e., the head is `None`), the function should return `(0, 0)`.
"""

def calculate_length_and_sum(head):
    if head is None:
        return 0, 0
    
    length = 0
    total_sum = 0
    current = head
    
    while current is not None:
        length += 1
        total_sum += current.data
        current = current.next
        
    return length, total_sum
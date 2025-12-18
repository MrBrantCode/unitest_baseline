"""
QUESTION:
Create a function named `print_doubly_linked_list_reverse` that takes a node of a doubly linked list as an argument and prints the elements of the list in reverse order without using any extra space. The function should have a time complexity of O(n), where n is the number of nodes in the doubly linked list, and should use a recursive approach.
"""

def print_doubly_linked_list_reverse(node):
    if node is None:  
        return
    
    print_doubly_linked_list_reverse(node.next)
    
    print(node.data)
"""
QUESTION:
Design a Python function `linked_list_to_2d_list` that takes a list of linked list nodes as input, where each node has a 'value' attribute and a 'next' attribute. The function should return a two-dimensional list, where each inner list represents the values of a linked list in the input list.
"""

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def linked_list_to_2d_list(node_list):
    """
    Converts a list of linked lists to a 2D list.
    
    Args:
    node_list (list): A list of Node objects, each representing the head of a linked list.
    
    Returns:
    list: A 2D list where each inner list represents the values of a linked list in the input list.
    """
    two_dim_list = []
    
    for node in node_list:
        temp = node
        inner_list = []
        
        while temp:
            inner_list.append(temp.value)
            temp = temp.next
            
        two_dim_list.append(inner_list)
        
    return two_dim_list
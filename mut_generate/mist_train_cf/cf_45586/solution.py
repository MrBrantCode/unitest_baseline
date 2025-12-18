"""
QUESTION:
Write a function named `will_point_to_same_location` with two parameters, a pointer to the current node and a pointer to the next node. The function should determine whether two pointers will point to the same memory location after the following operations: the second pointer is set to the first pointer, and then the first pointer is set to the next node it points to.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def will_point_to_same_location(temp1, temp2):
    """
    This function determines whether two pointers will point to the same memory location 
    after the second pointer is set to the first pointer, and then the first pointer 
    is set to the next node it points to.

    Args:
        temp1 (Node): The first pointer.
        temp2 (Node): The second pointer.

    Returns:
        bool: True if the two pointers will point to the same memory location, False otherwise.
    """
    temp2 = temp1  # temp2 is made to point to the same location as temp1
    temp1 = temp1.next  # temp1 is assigned to point to the next node
    return temp1 == temp2  # check if temp1 and temp2 point to the same location
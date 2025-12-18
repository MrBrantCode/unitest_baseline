"""
QUESTION:
Swap adjacent nodes in a linked list. 
Create a function `swap_pairs` that takes the head of a linked list as input. 
Your function should return the head of the modified linked list where every two adjacent nodes are swapped. 
Assume that the linked list has an even number of nodes.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def swap_pairs(head):
    """
    This function takes the head of a linked list as input, 
    and returns the head of the modified linked list where every two adjacent nodes are swapped.

    :param head: The head of the linked list
    :return: The head of the modified linked list
    """
    # If the list is empty or only has one node, return the head
    if head is None or head.next is None:
        return head

    # Create a dummy node to keep track of the new head
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Iterate through the list with a gap of 2 nodes
    while head and head.next:
        # Store the first node
        first_node = head
        # Store the second node
        second_node = head.next

        # Swap the two nodes
        prev.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node

        # Move to the next pair of nodes
        prev = first_node
        head = first_node.next

    # Return the head of the modified list
    return dummy.next
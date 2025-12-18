"""
QUESTION:
Create a function `mergeLinkedLists(list1, list2)` that merges two sorted linked lists `list1` and `list2` in ascending order and removes any duplicate elements from the merged list. The function should return the head of the merged list. The linked list nodes are assumed to have a `val` attribute for the node value and a `next` attribute for the pointer to the next node.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeLinkedLists(list1, list2):
    """
    Merge two sorted linked lists in ascending order and remove any duplicate elements.

    Args:
        list1 (ListNode): The head of the first linked list.
        list2 (ListNode): The head of the second linked list.

    Returns:
        ListNode: The head of the merged linked list.
    """
    mergedList = ListNode()  # Create a new empty linked list
    current = mergedList  # Initialize a pointer for the merged list
    
    ptr1 = list1  # Initialize pointers for the two lists
    ptr2 = list2
    
    while ptr1 and ptr2:  # Traverse both lists simultaneously
        if ptr1.val <= ptr2.val:  # Compare values of the nodes
            current.next = ListNode(ptr1.val)  # Add smaller/equal value to the merged list
            ptr1 = ptr1.next  # Move pointer of the first list to the next node
        else:
            current.next = ListNode(ptr2.val)  # Add value from the second list to the merged list
            ptr2 = ptr2.next  # Move pointer of the second list to the next node
        current = current.next  # Move to the next node in the merged list
    
    # Append remaining nodes from the non-empty list to the merged list
    if ptr1:
        current.next = ptr1
    if ptr2:
        current.next = ptr2
    
    # Remove duplicates from the merged list
    current = mergedList.next
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    
    return mergedList.next  # Return the merged list
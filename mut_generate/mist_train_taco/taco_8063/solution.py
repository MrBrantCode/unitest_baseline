"""
QUESTION:
Given Pointer/Reference to the head of a doubly linked list of N nodes, the task is to Sort the given doubly linked list using Merge Sort in both non-decreasing and non-increasing order.
Example 1:
Input:
N = 8
value[] = {7,3,5,2,6,4,1,8}
Output:
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
Explanation: After sorting the given
linked list in both ways, resultant
matrix will be as given in the first
two line of output, where first line
is the output for non-decreasing
order and next line is for non-
increasing order.
Example 2:
Input:
N = 5
value[] = {9,15,0,-1,0}
Output:
-1 0 0 9 15
15 9 0 0 -1
Explanation: After sorting the given
linked list in both ways, the
resultant list will be -1 0 0 9 15
in non-decreasing order and 
15 9 0 0 -1 in non-increasing order.
Your Task:
The task is to complete the function sortDoubly() which sorts the doubly linked list. The printing is done automatically by the driver code.
Constraints:
1 <= N <= 10^{5}
"""

def sort_doubly_linked_list(head):
    # Helper function to convert the linked list to a list of values
    def linked_list_to_list(head):
        res = []
        while head:
            res.append(head.data)
            head = head.next
        return res
    
    # Helper function to create a doubly linked list from a list of values
    def list_to_doubly_linked_list(values):
        if not values:
            return None
        dummy = DoublyLinkedListNode(None)
        current = dummy
        for value in values:
            current.next = DoublyLinkedListNode(value)
            current.next.prev = current
            current = current.next
        head = dummy.next
        if head:
            head.prev = None
        return head
    
    # Convert the linked list to a list of values
    values = linked_list_to_list(head)
    
    # Sort the values in non-decreasing order
    sorted_asc_values = sorted(values)
    
    # Sort the values in non-increasing order
    sorted_desc_values = sorted(values, reverse=True)
    
    # Convert the sorted lists back to doubly linked lists
    sorted_asc = list_to_doubly_linked_list(sorted_asc_values)
    sorted_desc = list_to_doubly_linked_list(sorted_desc_values)
    
    return sorted_asc, sorted_desc
"""
QUESTION:
Given a linked list sorted in ascending order and an integer called data, insert data in the linked list such that the list remains sorted.
Example 1:
Input:
LinkedList: 25->36->47->58->69->80
data: 19
Output: 19 25 36 47 58 69 80
Example 2:
Input:
LinkedList: 50->100
data: 75
Output: 50 75 100
Your Task:
The task is to complete the function sortedInsert() which should insert the element in sorted Linked List and return the head of the linked list
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
Constraints:
1 <= N <= 10^{4}
-99999 <= A[i] <= 99999, for each valid i
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    new_node = Node(data)
    
    # If the list is empty or the new node should be inserted at the beginning
    if head is None or head.data > data:
        new_node.next = head
        head = new_node
        return head
    
    current = head
    while current.next is not None and current.next.data < data:
        current = current.next
    
    new_node.next = current.next
    current.next = new_node
    
    return head
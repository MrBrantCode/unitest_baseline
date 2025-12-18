"""
QUESTION:
Given two linked lists, your task is to complete the function makeUnion(), that returns the union list of two linked lists. This union list should include all the distinct elements only and it should be sorted in ascending order.
Example 1:
Input:
L1 = 9->6->4->2->3->8
L2 = 1->2->8->6->2
Output: 
1 2 3 4 6 8 9
Explaination: 
All the distinct numbers from two lists, when sorted forms the list in the output. 
Example 2:
Input:
L1 = 1->5->1->2->2->5
L2 = 4->5->6->7->1
Output: 
1 2 4 5 6 7
Explaination: 
All the distinct numbers from two lists, when sorted forms the list in the output.
Your Task:
The task is to complete the function makeUnion() which makes the union of the given two lists and returns the head of the new list.
Expected Time Complexity: O((N+M)*Log(N+M))
Expected Auxiliary Space: O(N+M)
Constraints:
1<=N,M<=10^{4}
"""

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def make_union(head1, head2):
    # Helper function to convert linked list to a list of values
    def linked_list_to_list(head):
        values = []
        while head:
            values.append(head.data)
            head = head.next
        return values
    
    # Helper function to convert a sorted list of values to a linked list
    def list_to_linked_list(sorted_values):
        dummy = ListNode()
        current = dummy
        for value in sorted_values:
            current.next = ListNode(value)
            current = current.next
        return dummy.next
    
    # Convert both linked lists to lists
    list1 = linked_list_to_list(head1)
    list2 = linked_list_to_list(head2)
    
    # Combine the lists, remove duplicates, and sort
    union_list = sorted(set(list1 + list2))
    
    # Convert the sorted list back to a linked list
    return list_to_linked_list(union_list)
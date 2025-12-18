"""
QUESTION:
Given a sorted linked list, delete all nodes that have duplicate numbers (all occurrences), leaving only numbers that appear once in the original list. 
Example 1:
Input: 
N = 8
Linked List = 23->28->28->35->49->49->53->53
Output: 
23 35
Explanation:
The duplicate numbers are 28, 49 and 53 which 
are removed from the list.
Example 2:
Input:
N = 6
Linked List = 11->11->11->11->75->75
Output: 
Empty list
Explanation:
All the nodes in the linked list have 
duplicates. Hence the resultant list 
would be empty.
Your task:
You don't have to read input or print anything. Your task is to complete the function removeAllDuplicates() which takes the head of the linked list, removes all the occurences of duplicates in the linked list and returns the head of the modified linked list.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 ≤ N ≤ 10^5
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_duplicates_from_sorted_list(head: ListNode) -> ListNode:
    if not head:
        return head
    
    dummy = ListNode(val=-69)
    dummy.next = head
    prev = dummy
    
    while prev.next and prev.next.next:
        if prev.next.val == prev.next.next.val:
            duplicate_val = prev.next.val
            while prev.next and prev.next.val == duplicate_val:
                prev.next = prev.next.next
        else:
            prev = prev.next
    
    return dummy.next
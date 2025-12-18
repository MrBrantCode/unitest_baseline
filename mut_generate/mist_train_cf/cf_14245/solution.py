"""
QUESTION:
Delete every third element from a sorted linked list while maintaining the ascending order of the remaining elements. The linked list node is defined as having a value and a pointer to the next node. Implement the function `delete_every_third_element(head)` where `head` is the head of the linked list, and return the head of the modified linked list. The function should handle the case when the input linked list is empty.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteEveryThirdElement(head):
    if not head:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    current = head
    count = 1

    while current:
        if count % 3 == 0:
            prev.next = current.next
        else:
            prev = current
        
        current = current.next
        count += 1

    return dummy.next
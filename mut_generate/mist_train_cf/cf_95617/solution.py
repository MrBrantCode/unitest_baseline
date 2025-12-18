"""
QUESTION:
Write a function `mergeLinkedLists(list1, list2)` that merges two linked lists (`list1` and `list2`) in ascending order and removes any duplicate elements from the merged list. The function should return the head of the merged linked list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeLinkedLists(list1, list2):
    mergedList = ListNode()  
    current = mergedList  
    
    ptr1 = list1  
    ptr2 = list2
    
    while ptr1 and ptr2:  
        if ptr1.val <= ptr2.val:  
            current.next = ListNode(ptr1.val)  
            ptr1 = ptr1.next  
        else:
            current.next = ListNode(ptr2.val)  
            ptr2 = ptr2.next  
        current = current.next  
    
    if ptr1:
        current.next = ptr1
    if ptr2:
        current.next = ptr2
    
    current = mergedList.next
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    
    return mergedList.next 
"""
QUESTION:
Implement a function named `merge_sort` to sort a doubly linked list in ascending order. The doubly linked list contains nodes with alphabetic characters. The `merge_sort` function should take the head of the doubly linked list as input and return the head of the sorted list. The sorting should be aligned with the English alphabetic sequence. The implementation should be able to handle a doubly linked list with any number of nodes.
"""

class Node: 
    def __init__(self, next=None, prev=None, data=None): 
        self.next = next 
        self.prev = prev 
        self.data = data 

def merge_sort(head):  
    if head is None or head.next is None: 
        return head 
   
    second = split(head) 
   
    head = merge_sort(head) 
    second = merge_sort(second) 
  
    return merge(head, second) 

def split(head): 
    fast = head 
    slow = head 
    while(True): 
        if fast.next is None: 
            break
        if fast.next.next is None: 
            break
        fast = fast.next.next
        slow = slow.next
    temp = slow.next
    slow.next = None
    return temp 
  
def merge(first, second): 
    if first is None: 
        return second  
    if second is None: 
        return first 
  
    if first.data < second.data: 
        first.next = merge(first.next, second) 
        first.next.prev = first 
        first.prev = None   
        return first 
    else: 
        second.next = merge(first, second.next) 
        second.next.prev = second  
        second.prev = None
        return second 
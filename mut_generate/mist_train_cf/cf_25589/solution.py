"""
QUESTION:
Write a function `detectLoop` that takes the head of a linked list as input and returns 1 if a loop exists in the list and 0 otherwise. The function should use Floyd's cycle detection algorithm (tortoise and the hare algorithm) to detect the loop. The function should assume that the linked list nodes have a `next` attribute.
"""

def detectLoop(head): 
    slow_p = head  
    fast_p = head  
  
    while (slow_p and fast_p and 
             fast_p.next): 
        slow_p = slow_p.next
        fast_p = fast_p.next.next
          
        if slow_p == fast_p: 
            return 1
  
    return 0
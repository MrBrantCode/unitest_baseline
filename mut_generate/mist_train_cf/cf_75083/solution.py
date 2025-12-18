"""
QUESTION:
Write a function called `removeDuplicates` that takes the head of a linked list as input and returns the head of the linked list with all duplicates removed. The function should not use any temporary buffer or extra space. The linked list is unsorted and may be empty or contain only one node.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeDuplicates(head):
    if head is None or head.next is None:
        return head

    currentIter = head
    while currentIter is not None:
        runner = currentIter
        while runner.next is not None:
            if runner.next.val == currentIter.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        currentIter = currentIter.next
    return head
"""
QUESTION:
Implement a function `mergeSortLinkedList` to sort a linked list using the Merge Sort algorithm. The function should take the head of the linked list as input and return the head of the sorted linked list. The function must not use any additional space that scales with the input size.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeSortLinkedList(head):
    if not head or not head.next:
        return head

    mid = getMiddle(head)
    midNext = mid.next

    mid.next = None

    left = mergeSortLinkedList(head)
    right = mergeSortLinkedList(midNext)

    sortedList = sortedMerge(left, right)
    return sortedList

def sortedMerge(a, b):
    result = None

    if not a:
        return b
    if not b:
        return a

    if a.val <= b.val:
        result = a
        result.next = sortedMerge(a.next, b)
    else:
        result = b
        result.next = sortedMerge(a, b.next)
    return result

def getMiddle(head):
    if not head:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow
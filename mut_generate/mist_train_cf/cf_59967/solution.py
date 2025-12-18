"""
QUESTION:
Design a function `mergeSort(head)` that sorts the elements of a linked list in ascending order using the merge sort algorithm. The function should take the head of the linked list as input, split it into two halves, recursively sort each half, and then merge the two sorted halves into a single sorted list. The function should return the head of the sorted linked list. The linked list node is defined as a class with `val` and `next` attributes, where `val` is the node's value and `next` is a reference to the next node in the list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeSort(head):
    if head is None or head.next is None:
        return head

    mid = middleNode(head)
    left_half = head
    right_half = mid.next
    mid.next = None

    return merge(mergeSort(left_half), mergeSort(right_half))


def middleNode(head):
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge(head1, head2):
    dummyNode = ListNode(0)
    currentNode = dummyNode
    while head1 is not None and head2 is not None:
        if head1.val < head2.val:
            currentNode.next = head1
            head1 = head1.next
        else:
            currentNode.next = head2
            head2 = head2.next

        currentNode = currentNode.next

    if head1 is not None:
        currentNode.next = head1
    else:
        currentNode.next = head2

    return dummyNode.next
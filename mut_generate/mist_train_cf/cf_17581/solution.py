"""
QUESTION:
Implement a function named `sort` that sorts a singly linked list in ascending order in-place. Each node of the linked list contains an integer value and the input linked list is guaranteed to have at least two nodes. The linked list can contain duplicates, have a maximum of 1000 nodes, and the values of the nodes can range from -1000 to 1000. The solution should not use any additional data structures such as arrays or hash maps and should be optimized for both time and space complexity.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def split(head):
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    second_half = slow.next
    slow.next = None

    return second_half

def merge(l1, l2):
    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next

        current = current.next

    current.next = l1 or l2

    return dummy.next

def sort(head):
    if not head or not head.next:
        return head

    second_half = split(head)
    sorted_first_half = sort(head)
    sorted_second_half = sort(second_half)

    return merge(sorted_first_half, sorted_second_half)
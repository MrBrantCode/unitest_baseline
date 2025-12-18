"""
QUESTION:
Implement a function named `sort(head)` that sorts a singly linked list in ascending order in place. The linked list contains nodes with integer values and has at least two nodes. The function should not use any additional data structures such as arrays or hash maps and should be optimized for both time and space complexity. The input linked list can contain duplicates and have up to 1000 nodes with values ranging from -1000 to 1000.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sort(head):
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

    if not head or not head.next:
        return head

    second_half = split(head)
    sorted_first_half = sort(head)
    sorted_second_half = sort(second_half)

    return merge(sorted_first_half, sorted_second_half)
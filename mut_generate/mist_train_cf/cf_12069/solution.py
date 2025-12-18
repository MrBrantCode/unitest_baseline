"""
QUESTION:
Write a function `sort_linked_list` that sorts a singly linked list in ascending order. The function should be efficient for large lists and preserve the relative order of equal elements. It should also minimize the number of writes to memory. The input is the head of the linked list, and the output is the head of the sorted linked list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortLinkedList(head):
    # Merge sort function to sort the linked list
    def merge_sort(head):
        if not head or not head.next:
            return head
        mid = get_middle(head)
        left = merge_sort(head)
        right = merge_sort(mid)
        return merge(left, right)

    # Function to merge two sorted linked lists
    def merge(head1, head2):
        dummy = ListNode(0)
        current = dummy
        while head1 and head2:
            if head1.val < head2.val:
                current.next = head1
                head1 = head1.next
            else:
                current.next = head2
                head2 = head2.next
            current = current.next
        current.next = head1 or head2
        return dummy.next

    # Function to find the middle of a linked list
    def get_middle(head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid

    return merge_sort(head)
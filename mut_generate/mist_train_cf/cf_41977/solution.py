"""
QUESTION:
Implement the function `isPalindrome` that takes the head of a singly linked list as input, where each node is represented as `ListNode(data=0, next=None)`, and returns `True` if the linked list is a palindrome, and `False` otherwise.
"""

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def is_palindrome(head: ListNode) -> bool:
    # Function to reverse a linked list
    def reverseLinkedList(node):
        prev = None
        current = node
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    # Function to find the middle of the linked list
    def findMiddle(node):
        slow = node
        fast = node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Reverse the second half of the linked list
    middle = findMiddle(head)
    second_half = reverseLinkedList(middle)

    # Compare the first and second halves of the linked list
    while second_half:
        if head.data != second_half.data:
            return False
        head = head.next
        second_half = second_half.next
    return True
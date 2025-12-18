"""
QUESTION:
Write a function named `get_intersection` that takes the heads of two unsorted linked lists as input and returns the intersection node of the two linked lists. The function should not use any extra space and should not modify the input linked lists. The time complexity of the function should be O(n + m), where n and m are the lengths of the two linked lists.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def get_intersection(head1, head2):
    # Base case
    if head1 is None or head2 is None:
        return None

    # Find the length of the first linked list
    len1 = get_length(head1)

    # Find the length of the second linked list
    len2 = get_length(head2)

    # Move the pointer of the longer linked list to make the lengths equal
    if len1 > len2:
        for _ in range(len1 - len2):
            head1 = head1.next
    else:
        for _ in range(len2 - len1):
            head2 = head2.next

    # Move both pointers until they meet or reach the end
    while head1 is not None and head2 is not None:
        if head1 == head2:
            return head1
        head1 = head1.next
        head2 = head2.next

    # No intersection found
    return None

def get_length(head):
    length = 0
    while head is not None:
        length += 1
        head = head.next
    return length
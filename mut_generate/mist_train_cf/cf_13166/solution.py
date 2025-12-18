"""
QUESTION:
Create a function `findIntersectionNode(list1, list2)` that determines if two linked lists intersect at a specific node with a prime number value. The function should return `True` if such an intersection exists, and `False` otherwise. The linked lists are represented by their head nodes.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findIntersectionNode(list1, list2):
    def isPrime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def getLinkedListLength(head):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        return length

    def getIntersectionNode(head1, head2):
        length1 = getLinkedListLength(head1)
        length2 = getLinkedListLength(head2)

        diff = abs(length1 - length2)
        longer = head1 if length1 > length2 else head2
        shorter = head2 if length1 > length2 else head1

        for _ in range(diff):
            longer = longer.next

        while longer and shorter:
            if longer.val == shorter.val and isPrime(longer.val):
                return longer
            longer = longer.next
            shorter = shorter.next

        return None

    return getIntersectionNode(list1, list2) is not None
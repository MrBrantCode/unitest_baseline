"""
QUESTION:
Create a function called `findIntersectionNode` that determines if two linked lists intersect at a node with a prime value. The function takes two linked list heads, `list1` and `list2`, as input and returns a boolean indicating whether an intersection node with a prime value exists.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

def findIntersectionNode(list1, list2):
    length1 = getLinkedListLength(list1)
    length2 = getLinkedListLength(list2)

    diff = abs(length1 - length2)
    longer = list1 if length1 > length2 else list2
    shorter = list2 if length1 > length2 else list1

    for _ in range(diff):
        longer = longer.next

    while longer and shorter:
        if longer.val == shorter.val and isPrime(longer.val):
            return True
        longer = longer.next
        shorter = shorter.next

    return False
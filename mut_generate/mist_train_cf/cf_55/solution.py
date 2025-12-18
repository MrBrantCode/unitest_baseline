"""
QUESTION:
Implement a function `access_nth_from_end(head, n)` that takes the head node of a doubly linked list and an integer `n` as input and returns the value of the nth element from the end of the linked list. The function should have a time complexity of O(n) and should not use any additional data structures, recursion, or built-in methods to access the elements of the linked list. Assume the linked list has at least `n` elements and its structure cannot be modified.
"""

def access_nth_from_end(head, n):
    fast = head
    slow = head

    # Move the fast pointer n positions forward
    for _ in range(n):
        fast = fast.next

    # Check if the fast pointer reaches the end of the linked list
    if fast is None:
        return None  

    # Move both pointers simultaneously until the fast pointer reaches the end
    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    # Return the value of the node pointed to by the slow pointer
    return slow.value
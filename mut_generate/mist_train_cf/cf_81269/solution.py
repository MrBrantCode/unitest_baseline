"""
QUESTION:
Design a function named `rotate` for a doubly linked list that takes an integer `N` as input and rotates the list to the right by `N` nodes. The function should handle cases where `N` is larger than the length of the list and also accept negative values for `N`. If `N` is larger than the length of the list, return an error message.
"""

def rotate(self, N):
    if N < 0:
        N = -N
    if not self.head or N == 0:
        return
    cur_node = self.head
    count = 1
    while count < N and cur_node:
        cur_node = cur_node.next
        count += 1
    if not cur_node:
        print("N is larger than the length of the list.")
        return
    cur_node.next.prev = None
    cur_node.next, last_node = self.head, cur_node.next
    while cur_node.next:
        cur_node = cur_node.next
    cur_node.next = last_node
    last_node.prev = cur_node
    self.head = last_node
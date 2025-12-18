"""
QUESTION:
Implement a function `remove_element` that takes a singly linked list and a value `k` as input, and removes all instances of `k` from the list. The function should modify the original list and handle cases where the head node is the node to be removed.
"""

def remove_element(self, k):
    # If the list is empty
    if not self.head:
        return

    # If the head matches the element to be removed
    while self.head and self.head.data == k:
        self.head = self.head.next

    # Otherwise, check the rest of the list, keep track of the current node and the next node
    curr_node = self.head
    while curr_node and curr_node.next:
        # If next node's data is k, then skip it by pointing its previous node's next to the node after
        if curr_node.next.data == k:
            curr_node.next = curr_node.next.next
        else:
            curr_node = curr_node.next
"""
QUESTION:
Implement a method named `remove_node` that takes a `key` as input and removes the node with matching data from a doubly-linked list. The method should reconnect the previous node with the next node to maintain the list's integrity. It should return the values of the removed node's previous and next nodes. If the node is not found, return `None` for both values. Assume all node values are unique.
"""

def remove_node(head, key):
    curr = head
    while curr is not None:
        if curr.data == key:
            prev_node = curr.prev
            next_node = curr.next
            # If node to be removed is head node
            if curr.prev is None:
                head = curr.next
                curr.next.prev = None
            # If the node to be removed is not head and not tail
            elif curr.next is not None:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
            # If node to be removed is the tail
            else:
                curr.prev.next = None
            return prev_node.data if prev_node else None, next_node.data if next_node else None
        curr = curr.next
    return None, None  # if the node is not found
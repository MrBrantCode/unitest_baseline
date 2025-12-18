"""
QUESTION:
Write a function `delete_nodes` in a LinkedList class that deletes all occurrences of a given node value from a non-empty linked list and returns the number of deleted nodes.
"""

def delete_nodes(self, value):
    count = 0
    while self.head and self.head.value == value:
        self.head = self.head.next
        count += 1

    curr_node = self.head
    while curr_node and curr_node.next:
        if curr_node.next.value == value:
            curr_node.next = curr_node.next.next
            count += 1
        else:
            curr_node = curr_node.next

    return count
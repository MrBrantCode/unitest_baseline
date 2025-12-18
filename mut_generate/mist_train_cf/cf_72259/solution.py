"""
QUESTION:
Implement a `get_nth_last_node` function in a linked list that returns the nth last element. The function should handle edge cases where the linked list is empty or 'n' is larger than the size of the linked list. The function should achieve optimal time and space complexity. The function takes two parameters: `self` (the linked list object) and `n` (the position of the node from the end of the list), and returns the data of the nth last node, or None if 'n' is larger than the list size or the list is empty.
"""

def get_nth_last_node(self, n):
    p1 = p2 = self.head
    for _ in range(n):
        if p2 is None:
            return None
        p2 = p2.next
    while p2:
        p1 = p1.next
        p2 = p2.next
    return p1.data if p1 else None
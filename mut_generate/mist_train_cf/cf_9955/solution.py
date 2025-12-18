"""
QUESTION:
Implement a `insert` function in a singly-linked list that accepts a `value` and a `position` as parameters, inserts the `value` at the specified `position` in the list, and returns the updated list. The `position` must be a valid index within the list. If the `position` is out of bounds, the function should handle it accordingly. The function should work correctly for cases where the list is empty or the `position` is 0.
"""

def insert(self, value, position):
    new_node = Node(value)

    if self.head is None:
        self.head = new_node
        return self.head

    if position == 0:
        new_node.next = self.head
        self.head = new_node
        return self.head

    current = self.head
    prev = None
    count = 0

    while current and count < position:
        prev = current
        current = current.next
        count += 1

    if count == position:
        prev.next = new_node
        new_node.next = current
    else:
        print("Index out of bounds")

    return self.head
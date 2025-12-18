"""
QUESTION:
Create a function called `insert_sorted` that inserts a new element into a singly-linked list while maintaining sorted order. The function should first check if the list is already sorted, and if not, sort it before inserting the new element. Additionally, the function should handle duplicates based on a boolean flag: if `True`, insert the duplicate; if `False`, skip it. The function should not create a new list or alter the existing list's size unnecessarily. The `insert_sorted` function should take two parameters: `data` (the new element to be inserted) and `allow_duplicates` (the boolean flag for handling duplicates).
"""

def insert_sorted(self, data, allow_duplicates):
    if self.head is None:
        self.head = Node(data)
        return

    if not self.is_sorted():
        self.sort_list()

    if not allow_duplicates and self.is_duplicate(data):
        return 

    if data < self.head.data:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    else:
        current = self.head
        while current.next is not None and current.next.data < data:
            current = current.next
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
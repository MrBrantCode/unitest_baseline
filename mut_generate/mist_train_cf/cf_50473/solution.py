"""
QUESTION:
Create a function `delete` that takes a key as input and removes the node with the corresponding value from a linked list. The function should work for a linked list where each node has a `data` attribute and a `next` attribute pointing to the next node in the list. If the key is not found in the list, the function should do nothing. The function should be efficient and assume that the given key exists in the linked list.
"""

def delete(self, key):
    head = self.head
    if head is not None:
        if head.data == key:
            self.head = head.next
            head = None
            return
    while head is not None:
        if head.data == key:
            break
        prev = head
        head = head.next
    if head == None:
        return
    prev.next = head.next
    head = None
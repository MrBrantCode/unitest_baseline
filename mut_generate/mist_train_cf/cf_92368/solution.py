"""
QUESTION:
Implement a function called `delete_at_middle(self, position)` that deletes a node at a specific position in a doubly linked list. The function should correctly update the `prev` and `next` pointers of the adjacent nodes and return the data of the deleted node. The position is 1-indexed. If the node at the specified position does not exist, the function should return `None`.
"""

def delete_at_middle(self, position):
    if self.head is None:
        return None
    else:
        if position == 1:
            temp = self.head
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
            return temp.data
        else:
            current = self.head
            count = 1
            while count < position - 1 and current.next is not None:
                current = current.next
                count += 1

            if current.next is not None:
                temp = current.next
                current.next = current.next.next
                if current.next is not None:
                    current.next.prev = current
                else:
                    self.tail = current
                return temp.data
            else:
                return None
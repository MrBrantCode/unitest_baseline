"""
QUESTION:
Implement a function named `sortedInsert` for a singly linked list. The function should take an integer `newData` as input, insert a new node with `newData` at the head of the linked list if `newData` is even, and maintain the sorted order of the linked list. If `newData` is odd, the function should not insert a new node.
"""

def sortedInsert(self, newData):
    if newData % 2 != 0:
        return
        
    newNode = Node(newData)
    if self.head is None:
        newNode.next = self.head
        self.head = newNode
            
    elif self.head.data >= newNode.data:
        newNode.next = self.head
        self.head = newNode
            
    else:
        current = self.head
        while (current.next is not None and
            current.next.data < newNode.data):
            current = current.next

        newNode.next = current.next
        current.next = newNode
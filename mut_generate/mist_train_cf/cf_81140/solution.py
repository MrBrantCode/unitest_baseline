"""
QUESTION:
Design a function `MultiplyTwoLinkedList` that multiplies two numbers represented by doubly linked lists. Each digit of the number is stored in a node in the list, in normal order, with the 1's digit at the end of the list. The function should return a new doubly linked list representing the product of the two input numbers.

The input linked lists consist of nodes with integer data, and `next` and `prev` pointers. The function should not modify the input linked lists. 

The digits in the output linked list should also be in normal order, with the 1's digit at the end of the list.
"""

# Node Creation
class Node: 
     def __init__(self, data):
           self.data = data  
           self.next = None 
           self.prev = None 
        
# Doubly Link List Creation      
class DoublyLinkedList: 
    def __init__(self): 
        self.head = None

    # Function to convert a doubly link list to a number
    def LinkedListToNumber(self): 
        num = 0
        temp = self.head 
        while temp:
            num = num*10+ temp.data
            temp = temp.next
        return num 

    # Function to convert a number to the doubly link list and return it
    @staticmethod
    def NumberToLinkedList(num): 
        num_str = str(num)
        dll = DoublyLinkedList()
        for digit in num_str: 
            node = Node(int(digit))
            if dll.head is None: 
                dll.head = node 
            else: 
                last = dll.head 
                while last.next: 
                    last = last.next
                last.next = node 
                node.prev = last 
        return dll 

def MultiplyTwoLinkedList(dll1, dll2):
    # Convert Doubly Linked List to number
    num1 = dll1.LinkedListToNumber()
    num2 = dll2.LinkedListToNumber()
    # Multiply two numbers
    product = num1 * num2
    # Convert multiplied number into Doubly Linked List
    product_dll = DoublyLinkedList.NumberToLinkedList(product)
    return product_dll
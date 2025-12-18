"""
QUESTION:
Add two linked lists of different sizes, where each node contains multiple digits and the digits are stored in reverse order, and return the resulting sum stored in a linked list in reverse order. The linked lists can have a maximum of 5 digits in each node. The function should take two linked lists as input and return a linked list as output. The function name should be `add_linked_lists(list1, list2)`.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def add_two_numbers(l1, l2):
    # Helper function to convert a number into a linked list
    def convert_to_linked_list(num):
        head = None
        curr = None
        while num > 0:
            digit = num % 10
            num //= 10
            new_node = Node(digit)
            if head is None:
                head = new_node
            else:
                curr.next = new_node
            curr = new_node
        return head

    # Helper function to convert a linked list into a number
    def convert_to_number(head):
        num = 0
        multiplier = 1
        while head is not None:
            num += head.data * multiplier
            multiplier *= 10
            head = head.next
        return num

    # Convert the given lists to numbers
    num1 = convert_to_number(l1)
    num2 = convert_to_number(l2)

    # Calculate the sum
    sum = num1 + num2

    # Convert the sum back to a linked list
    return convert_to_linked_list(sum)
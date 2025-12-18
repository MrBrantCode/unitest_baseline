"""
QUESTION:
Implement a Rectangle class in Python with the following properties and methods:

- The class takes two parameters, length and width, which are stored as positive integers and must not exceed 100 units.
- The class has a method to compute the area of the rectangle in constant time complexity.
- The class has a method to compute the perimeter of the rectangle in constant time complexity.
- The class has a method to check if the rectangle is a square or not.
- The class has a method to rotate the rectangle by 90 degrees clockwise in constant time complexity without requiring any additional memory allocation.
- The class has a method to check if the rectangle is a golden rectangle or not. A rectangle is considered a golden rectangle if the ratio of its longer side to its shorter side is approximately equal to 1.61803398875.
- The length and width should be represented using a custom data structure called "BigInt" which is implemented as a linked list, and this data structure should be able to handle integers of any size and support addition and subtraction operations.
"""

class BigIntNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class BigInt:
    def __init__(self, num_str):
        self.head = None
        self.tail = None
        for digit in num_str:
            self.add_digit(int(digit))

    def add_digit(self, digit):
        new_node = BigIntNode(digit)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def __str__(self):
        curr = self.head
        result = ""
        while curr:
            result += str(curr.value)
            curr = curr.next
        return result

def entance(length, width):
    length = BigInt(str(length))
    width = BigInt(str(width))
    area = int(str(length)) * int(str(width))
    perimeter = 2 * (int(str(length)) + int(str(width)))
    is_square = str(length) == str(width)
    longer_side = max(int(str(length)), int(str(width)))
    shorter_side = min(int(str(length)), int(str(width)))
    ratio = longer_side / shorter_side
    is_golden_rectangle = abs(ratio - 1.61803398875) < 1e-10
    return area, perimeter, is_square, is_golden_rectangle
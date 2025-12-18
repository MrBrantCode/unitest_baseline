"""
QUESTION:
Let's give it a try! You have a linked list and you have to implement the functionalities push and pop of stack using this given linked list. Your task is to use the class as shown in the comments in the code editor and complete the functions push() and pop() to implement a stack. 
Example 1:
Input: 
push(2)
push(3)
pop()
push(4) 
pop()
Output: 3 4
Explanation: 
push(2)    the stack will be {2}
push(3)    the stack will be {2 3}
pop()      poped element will be 3,
           the stack will be {2}
push(4)    the stack will be {2 4}
pop()      poped element will be 4
Example 2:
Input: 
pop()
push(4)
push(5)
pop()
Output: -1 5
Your Task: You are required to complete two methods push() and pop(). The push() method takes one argument, an integer 'x' to be pushed into the stack and pop() which returns an integer present at the top and popped out from the stack. If the stack is empty then return -1 from the pop() method.
Expected Time Complexity: O(1) for both push() and pop().
Expected Auxiliary Space: O(1) for both push() and pop().
Constraints:
1 <= Q <= 100
1 <= x <= 100
"""

def simulate_stack_operations(operations):
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class MyStack:
        def __init__(self):
            self.head = None

        def push(self, data):
            new = Node(data)
            new.next = self.head
            self.head = new

        def pop(self):
            if self.head is None:
                return -1
            remove = self.head.data
            self.head = self.head.next
            return remove

    stack = MyStack()
    results = []

    for operation in operations:
        if operation[0] == 'push':
            stack.push(operation[1])
        elif operation[0] == 'pop':
            results.append(stack.pop())

    return results
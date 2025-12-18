"""
QUESTION:
You are given N elements and your task is to Implement a Stack in which you can get a minimum element in O(1) time.
Example 1:
Input:
push(2)
push(3)
pop()
getMin()
push(1)
getMin()
Output: 2 1
Explanation: In the first test case for
query 
push(2)  Insert 2 into the stack.
         The stack will be {2}
push(3)  Insert 3 into the stack.
         The stack will be {2 3}
pop()    Remove top element from stack 
         Poped element will be 3 the
         stack will be {2}
getMin() Return the minimum element
         min element will be 2 
push(1)  Insert 1 into the stack.
         The stack will be {2 1}
getMin() Return the minimum element
         min element will be 1
Your Task:
You are required to complete the three methods push() which takes one argument an integer 'x' to be pushed into the stack, pop() which returns an integer popped out from the stack, and getMin() which returns the min element from the stack. (-1 will be returned if for pop() and getMin() the stack is empty.)
Expected Time Complexity: O(1) for all the 3 methods.
Expected Auxiliary Space: O(1) for all the 3 methods.
Constraints:
1 <= Number of queries <= 100
1 <= values of the stack <= 100
"""

def min_stack_operations(operations, values):
    """
    Perform a series of stack operations and return the results of pop and getMin operations.

    Parameters:
    - operations: List[str] - A list of operations to perform on the stack.
    - values: List[int] - A list of values corresponding to the push operations.

    Returns:
    - List[int] - A list of results from pop and getMin operations.
    """
    stack = []
    min_ele = -1
    result = []
    value_index = 0

    for operation in operations:
        if operation.startswith("push"):
            x = values[value_index]
            value_index += 1
            if not stack:
                stack.append(x)
                min_ele = x
            elif x > min_ele:
                stack.append(x)
            else:
                topel = 2 * x - min_ele
                stack.append(topel)
                min_ele = x
        elif operation == "pop":
            if stack:
                if stack[-1] < min_ele:
                    a = min_ele
                    min_ele = 2 * min_ele - stack[-1]
                    if len(stack) == 1:
                        min_ele = -1
                    stack.pop()
                    result.append(a)
                else:
                    if len(stack) == 1:
                        min_ele = -1
                    result.append(stack.pop())
            else:
                result.append(-1)
        elif operation == "getMin":
            result.append(min_ele)
    
    return result
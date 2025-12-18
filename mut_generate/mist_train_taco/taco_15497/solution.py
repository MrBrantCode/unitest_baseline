"""
QUESTION:
Your task is to implement  2 stacks in one array efficiently. You need to implement 4 methods.
push1 : pushes element into first stack.
push2 : pushes element into second stack.
pop1 : pops element from first stack and returns the popped element. If first stack is empty, it should return -1.
pop2 : pops element from second stack and returns the popped element. If second stack is empty, it should return -1.
Example 1:
Input:
push1(2)
push1(3)
push2(4)
pop1()
pop2()
pop2()
Output:
3 4 -1
Explanation:
push1(2) the stack1 will be {2}
push1(3) the stack1 will be {2,3}
push2(4) the stack2 will be {4}
pop1()   the poped element will be 3 from stack1 and stack1 will be {2}
pop2()   the poped element will be 4 from stack2 and now stack2 is empty
pop2()   the stack2 is now empty hence returned -1.
Example 2:
Input:
push1(1)
push2(2)
pop1()
push1(3)
pop1()
pop1()
Output:
3 1 -1
Explanation:
push1(1) the stack1 will be {1}
push2(2) the stack2 will be {2}
pop1()   the poped element will be 1 from stack1 and stack1 will be empty
push1(3) the stack1 will be {3}
pop1()   the poped element will be 3 from stack1 and stack1 will be empty
pop1()   the stack1 is now empty hence returned -1.
Your Task:
You don't need to read input or print anything. You are required to complete the 4 methods push1, push2 which takes one argument an integer 'x' to be pushed into stack one and two and pop1, pop2 which returns the integer poped out from stack one and two. If no integer is present in the stack return -1.
Expected Time Complexity: O(1) for all the four methods.
Expected Auxiliary Space: O(1) for all the four methods.
Constraints:
1 <= Number of queries <= 10^{4}
1 <= Number of elements in the stack <= 100
The sum of elements in both the stacks < size of the given array
"""

def two_stacks_operations(arr, operations):
    """
    Perform a series of operations on two stacks implemented in a single array.

    Parameters:
    - arr (list): The array to be used for implementing the two stacks.
    - operations (list of tuples): Each tuple represents an operation. The first element of the tuple is the operation type ('push1', 'push2', 'pop1', 'pop2') and the second element is the value to be pushed (only for 'push1' and 'push2').

    Returns:
    - list: A list of results corresponding to the operations performed. For 'push1' and 'push2', the result is None. For 'pop1' and 'pop2', the result is the popped value or -1 if the stack is empty.
    """
    
    results = []
    
    for op in operations:
        if op[0] == 'push1':
            arr.insert(0, op[1])
            results.append(None)
        elif op[0] == 'push2':
            arr.append(op[1])
            results.append(None)
        elif op[0] == 'pop1':
            if arr:
                results.append(arr.pop(0))
            else:
                results.append(-1)
        elif op[0] == 'pop2':
            if arr:
                results.append(arr.pop())
            else:
                results.append(-1)
    
    return results
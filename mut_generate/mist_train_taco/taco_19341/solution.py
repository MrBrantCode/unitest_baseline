"""
QUESTION:
Implement a Stack using two queues q1 and q2.
Example 1:
Input:
push(2)
push(3)
pop()
push(4)
pop()
Output: 3 4
Explanation:
push(2) the stack will be {2}
push(3) the stack will be {2 3}
pop()   poped element will be 3 the 
        stack will be {2}
push(4) the stack will be {2 4}
pop()   poped element will be 4  
Example 2:
Input:
push(2)
pop()
pop()
push(3)
Output: 2 -1
Your Task:
Since this is a function problem, you don't need to take inputs. You are required to complete the two methods push() which takes an integer 'x' as input denoting the element to be pushed into the stack and pop() which returns the integer poped out from the stack(-1 if the stack is empty).
Expected Time Complexity: O(1) for push() and O(N) for pop() (or vice-versa).
Expected Auxiliary Space: O(1) for both push() and pop().
Constraints:
1 <= Number of queries <= 100
1 <= values of the stack <= 100
"""

def stack_operations(operations):
    q1 = []
    q2 = []
    results = []
    
    for op in operations:
        if op[0] == 'push':
            x = op[1]
            q1.append(x)
            while q2:
                val = q2.pop(0)
                q1.append(val)
            (q1, q2) = (q2, q1)
        elif op[0] == 'pop':
            if not q2:
                results.append(-1)
            else:
                results.append(q2.pop(0))
    
    return results
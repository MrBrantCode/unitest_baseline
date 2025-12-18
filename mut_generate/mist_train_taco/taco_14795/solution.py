"""
QUESTION:
Given elements of a stack, clone the stack without using extra space.
Example 1:
Input:
N = 10
st[] = {1, 1, 2, 2, 3, 4, 5, 5, 6, 7}
Output:
1 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function clonestack() which takes the input stack st[], an empty stack cloned[], you have to clone the stack st into stack cloned.
The driver code itself prints 1 in the output if the stack st is cloned properly and prints 0 otherwise.
Expected Time Complexity: O(N*N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 1000
1<= st[i] <= 10^{5}
"""

def clone_stack(st: list, cloned: list) -> None:
    """
    Clones the given stack `st` into the empty stack `cloned` without using extra space.

    Parameters:
    - st (list): The original stack to be cloned.
    - cloned (list): The empty stack where the cloned elements will be stored.

    Returns:
    - None: The function modifies the `cloned` stack in place.
    """
    while st:
        cloned.append(st.pop())
    while cloned:
        st.append(cloned.pop())
    while st:
        cloned.append(st.pop())
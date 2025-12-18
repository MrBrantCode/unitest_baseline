"""
QUESTION:
You are given a string S of size N that represents the prefix form of a valid mathematical expression. Convert it to its infix form.
Example 1:
Input: 
*-A/BC-/AKL
Output: 
((A-(B/C))*((A/K)-L))
Explanation: 
The above output is its valid infix form.
Your Task:
Complete the function string preToInfix(string pre_exp), which takes a prefix string as input and return its infix form.
 
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints:
3<=|S|<=10^{4}
"""

def prefix_to_infix(pre_exp: str) -> str:
    stk = []
    i = len(pre_exp) - 1
    while i >= 0:
        if pre_exp[i] in ['+', '-', '*', '/', '^']:
            op1 = stk.pop()
            op2 = stk.pop()
            stk.append(f'({op1}{pre_exp[i]}{op2})')
        else:
            stk.append(pre_exp[i])
        i -= 1
    return stk.pop()
"""
QUESTION:
You are given a string that represents the postfix form of a valid mathematical expression. Convert it to its infix form.
Example:
Input:
ab*c+ 
Output: 
((a*b)+c)
Explanation: 
The above output is its valid infix form.
Your Task:
Complete the function string postToInfix(string post_exp), which takes a postfix string as input and returns its infix form.
 
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints:
3<=post_exp.length()<=10^{4}
"""

def postfix_to_infix(post_exp: str) -> str:
    stk = []
    for char in post_exp:
        if char in ['*', '/', '-', '+', '^']:
            op1 = stk.pop()
            op2 = stk.pop()
            stk.append(f'({op2}{char}{op1})')
        else:
            stk.append(char)
    return stk.pop()
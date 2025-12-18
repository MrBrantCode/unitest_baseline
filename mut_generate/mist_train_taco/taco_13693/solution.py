"""
QUESTION:
You are given a string that represents the postfix form of a valid mathematical expression. Convert it to its prefix form.
Example:
Input: 
ABC/-AK/L-*
Output: 
*-A/BC-/AKL
Explanation: 
The above output is its valid prefix form.
Your Task:
Complete the function string postToPre(string post_exp), which takes a postfix string as input and returns its prefix form.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints:
3<=post_exp.length()<=1000
"""

def postfix_to_prefix(post_exp: str) -> str:
    """
    Converts a given postfix expression to its prefix form.

    Parameters:
    post_exp (str): The postfix expression to be converted.

    Returns:
    str: The prefix expression.
    """
    stack = []
    operators = {'^', '*', '/', '+', '-'}
    
    for char in post_exp:
        if char not in operators:
            stack.append(char)
        elif len(stack) >= 2:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(char + operand2 + operand1)
    
    return stack[0]
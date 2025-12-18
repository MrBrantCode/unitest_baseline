"""
QUESTION:
Given a string S, composed of different combinations of '(' , ')', '{', '}', '[', ']'. The task is to verify the validity of the arrangement.
An input string is valid if:
         1. Open brackets must be closed by the same type of brackets.
         2. Open brackets must be closed in the correct order.
Example 1:
Input:
S = ()[]{}
Output: 1
Explanation: The arrangement is valid.
 
Example 2:
Input:
S = ())({}
Output: 0
Explanation: Arrangement is not valid.
Example 3:
Input:
S = ([)]
Output: 0
Explanation: Arrangement is not valid.
 
Your Task:  
You dont need to read input or print anything. Complete the function valid() which takes S as input and returns a boolean value denoting whether the arrangement is valid or not.
Expected Time Complexity: O(N) where N is the length of S.
Expected Auxiliary Space: O(N) 
Constraints:
1 <= N <= 10^{4}
"""

def is_valid_parentheses(s: str) -> bool:
    """
    Determines if the given string of brackets is valid.

    Parameters:
    s (str): The string containing the brackets to be validated.

    Returns:
    bool: True if the arrangement of brackets is valid, False otherwise.
    """
    bracket_map = {'{': '}', '(': ')', '[': ']'}
    stack = []
    
    for bracket in s:
        if bracket in bracket_map:
            stack.append(bracket)
        elif stack and bracket_map[stack[-1]] == bracket:
            stack.pop()
        else:
            return False
    
    return len(stack) == 0
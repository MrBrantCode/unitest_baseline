"""
QUESTION:
Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).
Note: The drive code prints "balanced" if function return true, otherwise it prints "not balanced".
Example 1:
Input:
{([])}
Output: 
true
Explanation: 
{ ( [ ] ) }. Same colored brackets can form 
balanced pairs, with 0 number of 
unbalanced bracket.
Example 2:
Input: 
()
Output: 
true
Explanation: 
(). Same bracket can form balanced pairs, 
and here only 1 type of bracket is 
present and in balanced way.
Example 3:
Input: 
([]
Output: 
false
Explanation: 
([]. Here square bracket is balanced but 
the small bracket is not balanced and 
Hence , the output will be unbalanced.
Your Task:
This is a function problem. You only need to complete the function ispar() that takes a string as a parameter and returns a boolean value true if brackets are balanced else returns false. The printing is done automatically by the driver code.
Expected Time Complexity: O(|x|)
Expected Auixilliary Space: O(|x|)
Constraints:
1 ≤ |x| ≤ 32000
"""

def is_balanced_expression(expression: str) -> bool:
    open_brackets = ['{', '(', '[']
    close_brackets = ['}', ')', ']']
    stack = []
    
    for char in expression:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if len(stack) == 0:
                return False
            if close_brackets.index(char) == open_brackets.index(stack[-1]):
                stack.pop()
            else:
                return False
    
    return len(stack) == 0
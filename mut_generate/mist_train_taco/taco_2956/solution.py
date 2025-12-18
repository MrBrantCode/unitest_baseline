"""
QUESTION:
Given a string of balanced expression, find if it contains a redundant parenthesis or not. A set of parenthesis are redundant if the same sub-expression is surrounded by unnecessary or multiple brackets. Print Yes if redundant, else No.
Note: Expression may contain + , - , *, and / operators. Given expression is valid and there are no white spaces present.
Example 1:
Input:
exp = ((a+b))
Output:
Yes
Explanation:
((a+b)) can reduced to (a+b).
Example 2:
Input:
exp = (a+b+(c+d))
Output:
No
Explanation:
(a+b+(c+d)) doesn't have any redundant or multiple
brackets.
Your task:
You don't have to read input or print anything. Your task is to complete the function checkRedundancy() which takes the string s as input and returns 1 if it contains redundant parentheses else 0.
Constraints:
1<=|str|<=10^{4}
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
"""

def has_redundant_parentheses(exp: str) -> int:
    stack = []
    for char in exp:
        if char != ')':
            stack.append(char)
        else:
            count = 0
            while stack and stack[-1] != '(':
                stack.pop()
                count += 1
            if stack:
                stack.pop()  # Remove the corresponding '('
            if count <= 1:
                return 1
    return 0
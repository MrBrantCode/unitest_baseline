"""
QUESTION:
A valid parentheses string is either empty "", "(" + X + ")", or X + Y, where X and Y are valid parentheses strings, and + represents string concatenation.
For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = X + Y, with X and Y nonempty valid parentheses strings.
Given a valid parentheses string s, consider its primitive decomposition: s = P_{1} + P_{2} + ... + P_{k}, where P_{i} are primitive valid parentheses strings.
Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.
Example 1:
Input:
s = "(()())(())"
Output:
"()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:
Input:
s = "()()"
Output:
""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
Your Task:
You don't need to read input or print anything. Your task is to complete the function removeOuter() which takes a string s as inputs and returns s  after removing the outermost parentheses of every primitive string in the primitive decomposition of s . 
Expected Time Complexity: O(n)
Expected Space Complexity: O(n)
Constraint:
1 <= s.length <= 10^{5}
s[i] is either '(' or ')'
s is a valid parentheses string.
"""

def remove_outer_parentheses(s: str) -> str:
    opened = 0
    result = []
    
    for char in s:
        if char == '(':
            if opened > 0:
                result.append(char)
            opened += 1
        elif char == ')':
            opened -= 1
            if opened > 0:
                result.append(char)
    
    return ''.join(result)
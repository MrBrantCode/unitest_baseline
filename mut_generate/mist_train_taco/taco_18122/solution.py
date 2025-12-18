"""
QUESTION:
Given a string S consisting of only opening and closing curly brackets '{' and '}', find out the minimum number of reversals required to convert the string into a balanced expression.
A reversal means changing '{' to '}' or vice-versa.
Example 1:
Input:
S = "}{{}}{{{"
Output: 3
Explanation: One way to balance is:
"{{{}}{}}". There is no balanced sequence
that can be formed in lesser reversals.
Example 2:
Input: 
S = "{{}{{{}{{}}{{"
Output: -1
Explanation: There's no way we can balance
this sequence of braces.
Your Task:
You don't need to read input or print anything. Your task is to complete the function countRev() which takes the string S as the input parameter and returns the minimum number of reversals required to balance the bracket sequence. If balancing is not possible, return -1. 
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ |S| ≤ 10^{5}
"""

def min_reversals_to_balance(s: str) -> int:
    stack = []
    n = len(s)
    
    # Step 1: Use a stack to balance the brackets
    for char in s:
        if char == '{':
            stack.append('{')
        elif stack and stack[-1] == '{':
            stack.pop()
        else:
            stack.append('}')
    
    # Step 2: Count the unbalanced brackets
    t1 = sum(1 for char in stack if char == '}')
    t2 = len(stack) - t1
    
    # Step 3: Calculate the minimum reversals required
    if (t1 + t2) % 2 != 0:
        return -1
    
    if t1 % 2 == 0 and t2 % 2 == 0:
        return t1 // 2 + t2 // 2
    elif t1 % 2 == 1 and t2 % 2 == 1:
        return t1 // 2 + t2 // 2 + 2
    else:
        return -1
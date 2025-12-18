"""
QUESTION:
Given a string S consisting of opening and closing parenthesis '(' and ')'. Find length of the longest valid parenthesis substring.
A parenthesis string is valid if:
	For every opening parenthesis, there is a closing parenthesis.
	Opening parenthesis must be closed in the correct order.
Example 1:
Input: S = ((()
Output: 2
Explaination: The longest valid 
parenthesis substring is "()".
Example 2:
Input: S = )()())
Output: 4
Explaination: The longest valid 
parenthesis substring is "()()".
Your Task:
You do not need to read input or print anything. Your task is to complete the function maxLength() which takes string S as input parameter and returns the length of the maximum valid parenthesis substring.
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(|S|)
Constraints:
1 ≤ |S| ≤ 10^{5}
"""

def find_longest_valid_parenthesis_length(S: str) -> int:
    stack = []
    max_length = 0
    start_index = 0
    
    for i in range(len(S)):
        if S[i] == '(':
            stack.append(i)
        elif not stack:
            start_index = i + 1
        else:
            stack.pop()
            if not stack:
                max_length = max(max_length, i - start_index + 1)
            else:
                max_length = max(max_length, i - stack[-1])
    
    return max_length
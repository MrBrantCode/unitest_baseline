"""
QUESTION:
You are given a string S, the task is to reverse the string using stack.
 
Example 1:
Input: S="GeeksforGeeks"
Output: skeeGrofskeeG
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function reverse() which takes the string S as an input parameter and returns the reversed string.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
1 ≤ length of the string ≤ 100
"""

def reverse_string_using_stack(s: str) -> str:
    stack = []
    for char in s:
        stack.append(char)
    reversed_string = []
    while stack:
        reversed_string.append(stack.pop())
    return ''.join(reversed_string)
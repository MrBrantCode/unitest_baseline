"""
QUESTION:
Given a string S consisting only of opening and closing parenthesis 'ie '('  and ')', find out the length of the longest valid(well-formed) parentheses substring.
NOTE: Length of the smallest valid substring ( ) is 2.
Example 1:
Input: S = "(()("
Output: 2
Explanation: The longest valid 
substring is "()". Length = 2.
Example 2:
Input: S = "()(())("
Output: 6
Explanation: The longest valid 
substring is "()(())". Length = 6.
Your Task:  
You dont need to read input or print anything. Complete the function findMaxLen() which takes S as input parameter and returns the maxlength.
Expected Time Complexity:O(n)
Expected Auxiliary Space: O(1)   
Constraints:
1 <= |S| <= 10^{5}
"""

def find_max_len(s: str) -> int:
    open_count = 0
    close_count = 0
    max_len = 0
    
    # Traverse the string from left to right
    for char in s:
        if char == '(':
            open_count += 1
        else:
            close_count += 1
        
        if close_count == open_count:
            max_len = max(max_len, 2 * close_count)
        elif close_count > open_count:
            open_count = close_count = 0
    
    open_count = close_count = 0
    
    # Traverse the string from right to left
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '(':
            open_count += 1
        else:
            close_count += 1
        
        if close_count == open_count:
            max_len = max(max_len, 2 * close_count)
        elif open_count > close_count:
            open_count = close_count = 0
    
    return max_len
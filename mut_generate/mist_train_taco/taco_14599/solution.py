"""
QUESTION:
Given an integer N representing the number of pairs of parentheses, the task is to generate all combinations of well-formed(balanced) parentheses.
Example 1:
Input:
N = 3
Output:
((()))
(()())
(())()
()(())
()()()
Example 2:
Input:
N = 1
Output:
()
Your Task:  
You don't need to read input or print anything. Complete the function AllParenthesis() which takes N as input parameter and returns the list of balanced parenthesis.
Expected Time Complexity: O(2^{N} * N).
Expected Auxiliary Space: O(2*N*X), X = Number of valid Parenthesis.
Constraints: 
1 ≤ N ≤ 12
"""

def generate_balanced_parentheses(n):
    def util(o, c, s, ans):
        if o < 0 or c < 0:
            return
        if o == 0 and c == 0:
            ans.append(s)
            return
        if o == c:
            util(o - 1, c, s + '(', ans)
        else:
            util(o - 1, c, s + '(', ans)
            util(o, c - 1, s + ')', ans)

    ans = []
    util(n, n, '', ans)
    return ans
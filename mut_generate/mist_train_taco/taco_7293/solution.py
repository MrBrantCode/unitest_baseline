"""
QUESTION:
Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
For Example:
ab: Number of insertions required is 1. bab or aba
aa: Number of insertions required is 0. aa
abcd: Number of insertions required is 3. dcbabcd
Example 1:
Input:
abcd
Output:
3
Explanation:
Here we can append 3 characters in the 
beginning,and the resultant string will 
be a palindrome ("dcbabcd").
Example 2:
Input:
aba
Output:
0
Explanation:
Given string is already a pallindrome hence
no insertions are required.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function findMinInsertions() which takes string S as input parameters and returns minimimum numser of insertions required.
Expected Time Complexity: O(|S|^{2})
Expected Auxiliary Space: O(|S|^{2})
Constraints:
1 ≤ |S| ≤ 500
"""

def find_min_insertions(S: str) -> int:
    m = len(S)
    b = S[::-1]
    n = len(b)
    t = [[0 for i in range(n + 1)] for j in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == b[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i][j - 1], t[i - 1][j])
    
    lps = t[m][n]
    return len(S) - lps
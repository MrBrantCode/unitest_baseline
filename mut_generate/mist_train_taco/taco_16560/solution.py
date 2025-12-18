"""
QUESTION:
Given an array of lowercase strings A[] of size N, determine if the strings can be chained together to form a circle.
A string X can be chained together with another string Y if the last character of X is same as first character of Y. If every string of the array can be chained with exactly two strings of the array(one with the first character and second with the last character of the string), it will form a circle.
For example, for the array arr[] = {"for", "geek", "rig", "kaf"} the answer will be Yes as the given strings can be chained as "for", "rig", "geek" and "kaf"
Example 1:
Input:
N = 3
A[] = { "abc", "bcd", "cdf" }
Output:
0
Explaination:
These strings can't form a circle 
because no string has 'd'at the starting index.
Example 2:
Input:
N = 4
A[] = { "ab" , "bc", "cd", "da" }
Output:
1
Explaination:
These strings can form a circle 
of strings.
Your Task:
You don't need to read input or print output. Your task is to complete the function isCircle() which takes the length of the array N and the array A as input parameters and returns 1 if we can form a circle or 0 if we cannot.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints: 
1 ≤ N ≤ 10^{4}
1 ≤ Length of strings ≤ 20
"""

def can_form_circle(N, A):
    def dfs(node, adj, vis):
        vis[node] = 1
        for i in adj[node]:
            if not vis[i]:
                dfs(i, adj, vis)

    def detect_cycle(src, adj, mark):
        vis = [0] * 26
        dfs(src, adj, vis)
        for i in range(26):
            if not vis[i] and mark[i] == 1:
                return 0
        return 1

    mark = [0] * 26
    adj = [[] for _ in range(26)]
    in_degree = [0] * 26
    out_degree = [0] * 26
    
    for i in A:
        u = ord(i[0]) - ord('a')
        v = ord(i[-1]) - ord('a')
        adj[u].append(v)
        mark[u] = mark[v] = 1
        in_degree[v] += 1
        out_degree[u] += 1
    
    for i in range(26):
        if in_degree[i] != out_degree[i]:
            return 0
    
    return detect_cycle(ord(A[0][0]) - ord('a'), adj, mark)
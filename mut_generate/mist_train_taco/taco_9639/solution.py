"""
QUESTION:
Find the number of leaf nodes in a full k-ary tree of height m.
Note: You have to return the answer module 10^{9}+7.
 
Example 1:
Input:
k = 2, m = 2
Output:
4
Explanation:
A full Binary tree of height 2 has 4 leaf nodes. 
Example 2:
Input:
k = 2, m = 1
Output:
2
Explanation:
A full Binary tree of height 1 has 2 leaf nodes.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function karyTree() which takes 2 Integers k, and m as input and returns the number of leaf nodes in a full k-ary Tree.
 
Expected Time Complexity: O(log(m))
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= k,m <= 10^{8}
"""

def calculate_leaf_nodes(k: int, m: int) -> int:
    MOD = 1000000007
    ans = 1
    while m > 0:
        if m % 2 != 0:
            ans = (ans * k) % MOD
        m = m >> 1
        k = (k * k) % MOD
    return ans
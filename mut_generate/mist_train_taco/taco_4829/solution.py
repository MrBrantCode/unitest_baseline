"""
QUESTION:
You are given an array of n elements, initially all a[i] = 0. Q queries need to be performed. Each query contains three integers l, r, and x  and you need to change all a[i] to (a[i] | x) for all l ≤ i ≤ r.
Return the array after executing Q queries.
Example 1:
Input:
N=3, Q=2
U=[[1, 3, 1],
   [1, 3, 2]]
Output:
a[]={3,3,3}
Explanation: 
Initially, all elements of the array are 0. After execution of the
first query, all elements become 1 and after execution of the 
second query all elements become 3.
Example 2:
Input:
N=3, Q=2
U=[[1, 2, 1],
   [3, 3, 2]]
Output:
a[]={1,1,2}
Explanantion:
[0,0,0] => [1,1,0] => [1,1,2]
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function updateQuery() which takes the integer N,Q, and U a QX3 matrix containing the Q queries where U[i][0] is l_{i}, U[i][1] is r_{i} andU[i][2] is x_{i}.and it returns the final array a.
Expected Time Complexity: O(N)
Expected Space Complexity: O(N)
Constraints:
1<=N<=10^{5}
1<=Q<=10^{5}
1<=U[i][0] <= U[i][1]<=N
1<= U[i][2] <=10^{5}
"""

def update_query(N, Q, U):
    dp = [[0] * 17 for _ in range(N + 1)]
    
    for l, r, v in U:
        l -= 1
        r -= 1
        for i in range(17):
            if 1 << i & v:
                dp[l][i] += 1
                dp[r + 1][i] -= 1
    
    for i in range(1, N):
        for j in range(17):
            dp[i][j] += dp[i - 1][j]
    
    ans = []
    for i in range(N):
        c = 0
        for j in range(17):
            if dp[i][j] > 0:
                c |= 1 << j
        ans.append(c)
    
    return ans
"""
QUESTION:
Given two arrays X[] and Y[] of size M and N respectively. Find number of pairs such that x^{y} > y^{x} where x is an element from X[] and y is an element from Y[].
Example 1:
Input:
M = 3, N = 2
X[] = {2, 1, 6}, Y = {1, 5}
Output: 3
Explanation: There are total 3 pairs 
where pow(x, y) is greater than pow(y, x) 
Pairs are (2, 1), (2, 5) and (6, 1).
Example 2:
Input:
M = 3, N = 3
X[] = {10, 19, 18}, Y[] = {11, 15, 9}
Output: 2
Explanation: There are total 2 pairs 
where pow(x, y) is greater than pow(y, x) 
Pairs are (10, 11) and (10, 15).
Your Task:
You don't need to read input or print anything. Your task is to complete the function countPairs() which takes array X[], array Y[], m and n as input parameters and returns an integer denoting the number of pairs that are true to the given condition. 
Expected Time Complexity: O(N*logN + M*logM)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ M, N ≤ 10^{5}
1 ≤ X[i], Y[i] ≤ 10^{3}
"""

def count_pairs(X, Y, m, n):
    # Precompute the values of x^(1/x) and y^(1/y)
    for i in range(m):
        X[i] **= 1 / X[i]
    for i in range(n):
        Y[i] **= 1 / Y[i]
    
    # Sort the arrays
    X.sort()
    Y.sort()
    
    # Initialize pointers and result counter
    i = j = 0
    ans = 0
    
    # Count the pairs
    while i < m:
        if j == n:
            ans += n
        else:
            while j < n and X[i] > Y[j]:
                j += 1
            ans += j
        i += 1
    
    return ans
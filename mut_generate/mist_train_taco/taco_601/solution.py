"""
QUESTION:
Given two arrays A and B of positive integers of size N and M where N >= M, the task is to maximize the dot product by inserting zeros in the second array but you cannot disturb the order of elements.
Dot Product of array A and B of size N is A[0]*B[0] + A[1]*B[1]+....A[N]*B[N].
Example 1:
Input: N = 5, A[] = {2, 3, 1, 7, 8} 
       M = 3, B[] = {3, 6, 7}
Output: 107
Explanation: We get maximum dot product 
after inserting 0 at first and third 
positions in second array.
Maximum Dot Product : = A[i] * B[j] 
2*0 + 3*3 + 1*0 + 7*6 + 8*7 = 107
Example 2:
Input: N = 3, A[] = {1, 2, 3}
       M = 1, B[] = {4} 
Output: 12 
Explanation: We get maximum dot product
after inserting 0 at first and second
positions in second array. 
Maximum Dot Product : = A[i] * B[j] 
1*0 + 2*0 + 3*4 = 12
Your Task:  
You don't need to read input or print anything. Complete the function maxDotProduct() which takes N, M, array A and B as input parameters and returns the maximum value.
Expected Time Complexity: O(N*M)
Expected Auxiliary Space: O(N*M)
Constraints:
1 ≤ M ≤N ≤ 10^{3}
1 ≤ A[i], B[i] ≤ 10^{3}
"""

def max_dot_product(N, M, A, B):
    # Initialize a 2D DP array with -1
    dp = [[-1 for _ in range(M)] for _ in range(N)]
    
    def solve(i, j, d):
        # Base case: if we have reached the end of either array
        if i == N or j == M:
            return 0
        # If the value is already computed, return it
        if dp[i][j] != -1:
            return dp[i][j]
        # If we can still insert zeros
        if d > 0:
            dp[i][j] = max(A[i] * B[j] + solve(i + 1, j + 1, d), solve(i + 1, j, d - 1))
        else:
            dp[i][j] = A[i] * B[j] + solve(i + 1, j + 1, d)
        return dp[i][j]
    
    # Start the recursive function with initial parameters
    return solve(0, 0, N - M)
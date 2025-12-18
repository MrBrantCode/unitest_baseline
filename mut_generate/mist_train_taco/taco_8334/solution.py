"""
QUESTION:
Given an array called A[] of sorted integers having no duplicates, find the length of the Longest Arithmetic Progression (LLAP) in it.
Example 1:
Input:
N = 6
set[] = {1, 7, 10, 13, 14, 19}
Output: 4
Explanation: The longest arithmetic 
progression is {1, 7, 13, 19}.
Example 2:
Input:
N = 5
A[] = {2, 4, 6, 8, 10}
Output: 5
Explanation: The whole set is in AP.
Your Task:
You don't need to read input or print anything. Your task is to complete the function lenghtOfLongestAP() which takes the array of integers called set[] and n as input parameters and returns the length of LLAP.
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(N^{2})
Constraints:
1 ≤ N ≤ 1000
1 ≤ set[i] ≤ 10^{4}
"""

def length_of_longest_ap(A, n):
    if n <= 2:
        return n
    
    # Initialize a 2D list to store the lengths of APs ending at each pair of indices
    dp = [[2] * n for _ in range(n)]
    max_len = 2
    
    # Iterate over the array to fill the dp table
    for j in range(n - 2, 0, -1):
        i = j - 1
        k = j + 1
        while i >= 0 and k < n:
            if A[i] + A[k] < 2 * A[j]:
                k += 1
            elif A[i] + A[k] > 2 * A[j]:
                dp[i][j] = 2
                i -= 1
            else:
                dp[i][j] = dp[j][k] + 1
                max_len = max(max_len, dp[i][j])
                i -= 1
                k += 1
    
    return max_len
"""
QUESTION:
Given an array of integers, arr[] and a number, K.You can pair two numbers of the array if the difference between them is strictly less than K. The task is to find the maximum possible sum of such disjoint pairs (i.e., each element of the array can be used at most once). The Sum of P pairs is the sum of all 2P elements of pairs.
 
Example 1:
Input  : 
arr[] = {3, 5, 10, 15, 17, 12, 9}
K = 4
Output : 
62
Explanation :
Then disjoint pairs with difference less
than K are, (3, 5), (10, 12), (15, 17)
max sum which we can get is 
3 + 5 + 10 + 12 + 15 + 17 = 62
Note that an alternate way to form 
disjoint pairs is,(3, 5), (9, 12), (15, 17)
but this pairing produces less sum.
 
Example 2:
Input  : 
arr[] = {5, 15, 10, 300}
K = 12
Output : 
25
 
Your Task:  
You don't need to read, input, or print anything. Your task is to complete the function maxSumPairWithDifferenceLessThanK() which takes the array arr[], its size N, and an integer K as inputs and returns the maximum possible sum of disjoint pairs.
 
Expected Time Complexity: O(N. log(N))
Expected Auxiliary Space: O(N)
 
Constraints:
1 ≤ N ≤ 10^{5}
0 ≤ K ≤ 10^{5}
1 ≤ arr[i] ≤ 10^{4}
"""

def maxSumPairWithDifferenceLessThanK(arr, K):
    arr.sort()
    N = len(arr)
    dp = [0] * N
    dp[0] = 0
    
    for i in range(1, N):
        dp[i] = dp[i - 1]
        if arr[i] - arr[i - 1] < K:
            if i >= 2:
                dp[i] = max(dp[i], arr[i - 1] + dp[i - 2] + arr[i])
            else:
                dp[i] = max(dp[i], arr[i] + arr[i - 1])
    
    return dp[N - 1]
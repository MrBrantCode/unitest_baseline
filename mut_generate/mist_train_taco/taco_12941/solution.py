"""
QUESTION:
You are given an array arr of N integers. You need to find the maximum score of an array.
The score of an array is calculated as follows.
	Choose an integer i, 1<=i<=size of current array and add a[i-1] * a[i] * a[i+1] to the score.
	Delete a[i], on deleting a[i], i-1 and i+1 become adjacent. i.e i+1 becomes i and size of an array shrinks.
	Repeat the process till the size of an array becomes 0.
Note:  Assume an extra 1 at each boundary.
 
Example 1:
Input:
N = 2
arr = { 5, 10 }
Output: 
60
Explanation:
First choose i=1, Score = 1*5*10
Then choose i=1, Score+= 1*10*1,
Total = 60
Example 2:
Input:
N = 5
arr = { 1, 2, 3, 4, 5 }
Output: 
110
Your Task:
You do not need to read input or print anything. Your task is to complete the function maxProductSum() which takes the value N and the array as input parameters and returns maximum score of an array.
Expected Time Complexity: O(N^{3})
Expected Auxiliary Space: O(N^{2})
 
Constraints:
1 ≤ N ≤ 100
1 ≤ arr[i] ≤ 100000
"""

def max_product_sum(arr, n=None):
    if n is None:
        n = len(arr)
    
    B = [0] * (n + 2)
    B[0] = 1
    B[n + 1] = 1
    for i in range(1, n + 1):
        B[i] = arr[i - 1]
    
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    
    for length in range(1, n + 1):
        for left in range(1, n - length + 2):
            right = left + length - 1
            for last in range(left, right + 1):
                dp[left][right] = max(dp[left][right], dp[left][last - 1] + B[left - 1] * B[last] * B[right + 1] + dp[last + 1][right])
    
    return dp[1][n]
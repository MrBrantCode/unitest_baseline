"""
QUESTION:
Given an array A[] of N integers and a range(L, R). The task is to find the number of subarrays having sum in the range L to R (inclusive).
Example 1:
Input:
N = 3, L = 3, R = 8
A[] = {1, 4, 6}
Output: 
3
Explanation: 
The subarrays are [1,4], [4] and [6]
Example 2:
Input:
N = 4, L = 4, R = 13
A[] = {2, 3, 5, 8}
Output: 
6
Explanation: 
The subarrays are [2,3], [2,3,5], 
[3,5],[5], [5,8] and [8]
Your Task: 
You don't need to read input or print anything. Complete the function countSubarray( ) which takes the integer N , the array A[], the integer L and the integer R as input parameters and returns the number of subarays. 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{6}
1 ≤ A[] ≤ 10^{9}
1 ≤ L ≤ R ≤ 10^{15}
"""

def count_subarrays_in_range(A, N, L, R):
    def count_sub(arr, n, x):
        st = 0
        end = 0
        sum = 0
        cnt = 0
        while end < n:
            sum += arr[end]
            while st <= end and sum > x:
                sum -= arr[st]
                st += 1
            cnt += end - st + 1
            end += 1
        return cnt

    Rcnt = count_sub(A, N, R)
    Lcnt = count_sub(A, N, L - 1)
    return Rcnt - Lcnt
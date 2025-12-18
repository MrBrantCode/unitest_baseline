"""
QUESTION:
Given an array A[] of N integers. The task is to partition the array into four non-empty contiguous subarrays P, Q, R, and S such that each element of the array A[] should be present in any subarray.
Let W, X, Y, and Z be the sum of the elements in P, Q, R, and S respectively.
Find the smallest absolute difference between the maximum and the minimum among W, X, Y, and Z.
Example 1:
Input:
N = 5
A[] = [4,2,2,5,1]
Output: 4
Explanation: let partition the array 
P,Q,R,S = [4],[2,2],[5],[1]
W = 4, X = 4, Y = 5, Z = 1 
Differnce = max(W,X,Y,Z)-min(W,X,Y,Z)= 5-1 = 4 
Example 2:
Input:
N = 4
A[] = {4,4,4,4}
Output: 0
Explanation: 
There is only one way to partition 
the array. P,Q,R,S = [4],[4],[4],[4]
Your Task:
You don't need to read input or print anything. The task is to complete the function minDifference() which takes the integer N and the array A[] as inputs and returns the smallest absolute difference.
Expected Time Complexity: O(NLogN)
Expected Auxiliary Space: O(N)
Constraints:
4 < N < 10^{5}
1 < A[i] < 10^{9}
"""

def find_min_partition_difference(N, A):
    def partition(A, n):
        tmp = [(0, 0)]
        p = A[:]
        for i in range(1, n):
            p[i] += p[i - 1]
        for i in range(1, n):
            diff = 10 ** 18
            hi = i
            lo = 1
            ans = (0, 0)
            while lo <= hi:
                mid = (lo + hi) // 2
                x = p[mid - 1]
                y = p[i] - x
                if abs(x - y) < diff:
                    diff = abs(x - y)
                    ans = (x, y)
                if x > y:
                    hi = mid - 1
                else:
                    lo = mid + 1
            tmp.append(ans)
        return tmp

    x = partition(A, N)
    A.reverse()
    y = partition(A, N)
    y.reverse()
    ans = 10 ** 18
    for i in range(1, N - 2):
        ans = min(ans, max(x[i][0], x[i][1], y[i + 1][0], y[i + 1][1]) - min(x[i][0], x[i][1], y[i + 1][0], y[i + 1][1]))
    return ans
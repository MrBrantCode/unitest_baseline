"""
QUESTION:
You are given an array Arr of size N. You have to find the K-th largest sum of contiguous subarray within the array elements.
 
Example 1:
Input:
N = 3
K = 2
Arr = {3,2,1}
Output:
5
Explanation:
The different subarray sums we can get from the array
are = {6,5,3,2,1}. Where 5 is the 2nd largest.
 
Example 2:
Input:
N = 4
K = 3
Arr = {2,6,4,1}
Output:
11
Explanation:
The different subarray sums we can get from the array
are = {13,12,11,10,8,6,5,4,2,1}. Where 11 is the 3rd largest.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function kthLargest() which takes the array Arr[] and its size N as inputs and returns the Kth largest subarray sum.
 
Expected Time Complexity: O(N^{2} * log K)
Expected Auxiliary Space: O(K)
 
Constraints:
1 <= N <= 100
1 <= K <= (N*(N+1))/2
-10^{5} <= Arr[i] <= 10^{5}
Sum of N over all test cases doesn't exceed 1000.
Array may contain duplicate elements.
"""

from typing import List
import heapq

def kth_largest_subarray_sum(Arr: List[int], K: int) -> int:
    N = len(Arr)
    res = []
    size = K
    
    for i in range(N):
        sum = 0
        for j in range(i, N):
            sum += Arr[j]
            if len(res) < size:
                heapq.heappush(res, sum)
            elif res[0] < sum:
                heapq.heappop(res)
                heapq.heappush(res, sum)
    
    return res[0]
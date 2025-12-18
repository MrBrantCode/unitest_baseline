"""
QUESTION:
Given an array A[] of N positive integers. The task is to find the maximum of j - i subjected to the constraint of A[i] < A[j] and i < j.
 
Example 1:
Input:
N = 2
A[] = {1, 10}
Output:
1
Explanation:
A[0]<A[1] so (j-i) is 1-0 = 1.
Example 2:
Input:
N = 9
A[] = {34, 8, 10, 3, 2, 80, 30, 33, 1}
Output:
6
Explanation:
In the given array A[1] < A[7]
satisfying the required 
condition(A[i] < A[j]) thus giving 
the maximum difference of j - i 
which is 6(7-1).
 
Your Task:
The task is to complete the function maxIndexDiff() which finds and returns maximum index difference. Printing the output will be handled by driver code. Return 0 in case no such index is found.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{7}
0 ≤ A[i] ≤ 10^{9}
"""

def max_index_diff(A, N):
    if N == 0:
        return 0
    
    left = [0] * N
    right = [0] * N
    diff = 0
    
    # Fill the right array with the maximum values from the right to the left
    maxi = A[N - 1]
    for i in range(N - 1, -1, -1):
        if A[i] >= maxi:
            maxi = A[i]
        right[i] = maxi
    
    # Traverse the array to find the maximum difference
    i, j = 0, 0
    while i < N and j < N:
        if A[i] <= right[j]:
            diff = max(diff, j - i)
            j += 1
        else:
            i += 1
    
    return diff
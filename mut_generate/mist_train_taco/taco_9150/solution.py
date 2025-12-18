"""
QUESTION:
Given two sorted arrays A and B of size M and N respectively. Each array may have some elements in common with the other array. Find the maximum sum of a path from the beginning of any array to the end of any of the two arrays. We can switch from one array to another array only at the common elements.Both the arrays are sorted.
Note: Only one repeated value is considered in the valid path sum.
Example 1:
Input:
M = 5, N = 4
A[] = {2,3,7,10,12}
B[] = {1,5,7,8}
Output: 35
Explanation: The path will be 1+5+7+10+12
= 35.
Example 2:
Input:
M = 3, N = 3
A[] = {1,2,3}
B[] = {3,4,5}
Output: 15
Explanation: The path will be 1+2+3+4+5=15.
Your Task:
You don't need to read input or print anything. Complete the function max_path_sum() which takes the two arrays A and B along with their sizes M and N as input parameters. It returns the maximum path sum.
Expected Time Complexity: O(M + N)
Expected Auxiliary Space: O(1)
Constraints:
1 <= M,N <= 10^{4}
1 <= A[i], B[i] <= 10^{4}
"""

def max_path_sum(A, B, M, N):
    maxsumpath = []
    path1 = []
    path2 = []
    i = 0
    j = 0
    
    while i < M and j < N:
        if A[i] < B[j]:
            path1.append(A[i])
            i += 1
        elif B[j] < A[i]:
            path2.append(B[j])
            j += 1
        elif A[i] == B[j]:
            sum1 = sum(path1)
            sum2 = sum(path2)
            if sum1 >= sum2:
                maxsumpath += path1
            else:
                maxsumpath += path2
            maxsumpath += [A[i]]
            path1 = []
            path2 = []
            i += 1
            j += 1
    
    for k in range(i, M):
        path1.append(A[k])
    
    for k in range(j, N):
        path2.append(B[k])
    
    sum1 = sum(path1)
    sum2 = sum(path2)
    
    if sum1 >= sum2:
        maxsumpath += path1
    else:
        maxsumpath += path2
    
    return sum(maxsumpath)
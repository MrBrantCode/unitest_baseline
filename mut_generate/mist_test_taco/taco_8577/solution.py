"""
QUESTION:
Given an array A[ ] of N of  integers, find the distinct index of values that satisfy A + B = C + D where A,B,C & D are integers values in the array.
Note: As there may be multiple pairs satisfying the equation return lexicographically smallest order of  A, B, C and D and return all as -1 if there are no pairs satisfying the equation.
 
Example 1:
Input:
N = 7
A[] = {3, 4, 7, 1, 2, 9, 8}
Output:
0 2 3 5
Explanation:
A[0] + A[2] = 3+7 = 10
A[3] + A[5] = 1+9 = 10
Example 2:
Input:
N = 4
A[] = {424, 12, 31, 7}
Output:
-1 -1 -1 -1
Explanation:
There are no pairs satisfying the equation.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function satisfyEqn() which takes an Integer N and an array A[] of size N as input and returns a vector of 4 integers denoting A, B, C, and D respectively.
 
Expected Time Complexity: O(N^{2}*logN^{2})
Expected Auxiliary Space: O(N^{2})
 
Constraints:
1 <= N <= 500
1 <= A[i] <= 10^{5}
"""

def find_distinct_indices(A, N):
    d = {}
    pairs = []
    
    for i in range(N):
        for j in range(i + 1, N):
            sum_ij = A[i] + A[j]
            if sum_ij not in d:
                d[sum_ij] = [i, j]
            else:
                k, l = d[sum_ij]
                if i != k and i != l and j != k and j != l:
                    pairs.append([k, l, i, j])
    
    if not pairs:
        return [-1, -1, -1, -1]
    
    return min(pairs)
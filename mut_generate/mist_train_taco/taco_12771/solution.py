"""
QUESTION:
Given a binary matrix M of size n X m. Find the maximum area of a rectangle formed only of 1s in the given matrix. 
Example 1:
Input:
n = 4, m = 4
M[][] = {{0 1 1 0},
         {1 1 1 1},
         {1 1 1 1},
         {1 1 0 0}}
Output: 8
Explanation: For the above test case the
matrix will look like
0 1 1 0
1 1 1 1
1 1 1 1
1 1 0 0
the max size rectangle is 
1 1 1 1
1 1 1 1
and area is 4 *2 = 8.
Your Task: 
Your task is to complete the function maxArea which returns the maximum size rectangle area in a binary-sub-matrix with all 1’s. The function takes 3 arguments the first argument is the Matrix M[ ] [ ] and the next two are two integers n and m which denotes the size of the matrix M. 
Expected Time Complexity : O(n*m)
Expected Auixiliary Space : O(m)
Constraints:
1<=n,m<=1000
0<=M[][]<=1
Note:The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code.
"""

def max_rectangle_area(M, n, m):
    def maxrect(arr, n):
        ps = [1]
        for i in range(1, n):
            k = i - 1
            count = 1
            while k >= 0 and arr[i] <= arr[k] and (arr[i] != 0):
                count += ps[k]
                k -= ps[k]
            ps.append(count)
        ns = [1] * n
        for i in range(n - 2, -1, -1):
            k = i + 1
            count = 1
            while k < n and arr[i] <= arr[k] and (arr[i] != 0):
                count += ns[k]
                k += ns[k]
            ns[i] = count
        maxi = 0
        for i in range(n):
            maxi = max(maxi, (abs(ns[i] + ps[i]) - 1) * arr[i])
        return maxi

    arr = [0] * m
    maxi = 0
    for i in range(n):
        for j in range(m):
            if M[i][j] == 1:
                arr[j] += 1
            else:
                arr[j] = 0
        maxi = max(maxi, maxrect(arr, m))
    return maxi
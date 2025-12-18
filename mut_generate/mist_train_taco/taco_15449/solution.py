"""
QUESTION:
Given a matrix with n rows and m columns. Your task is to find the kth element which is obtained while traversing the matrix spirally. You need to complete the method findK which takes four arguments the first argument is the matrix A and the next two arguments will be n and m denoting the size of the matrix A and then the forth argument is an integer k. The function will return the kth element obtained while traversing the matrix spirally.
Example 1:
Input:
n = 4, m = 4, k = 10
A[][] = {{1  2  3  4},
         {5  6  7  8},
         {9  10 11 12},
         {13 14 15 16}}
Output:
14
Explanation:
The spiral order of matrix will look like 1->2->3->4->8->12->16->15->14->13->9->5->6->7->11->10. So the 10th element in this order is 14. 
Example 2:
Input:
n = 3, m = 3, k = 4
A[][] = {{1 2 3},
         {4 5 6},
         {7 8 9}}
Output:
6
Explanation:
The spiral order of matrix will look like 1->2->3->6->9->8->7->4->5. So the 4th element in this order is 6.
Your Task:
You only need to implement the given function findK(). Do not read input, instead use the arguments given in the function. Return the K'th element obtained by traversing matrix spirally.
Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)
Constraints:
1<=n,m<=10^{3}
1<=k<=n*m
"""

def find_kth_spiral_element(matrix, n, m, k):
    seen = [[False for _ in range(m)] for _ in range(n)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    x = 0
    y = 0
    di = 0
    b = 1
    
    for _ in range(n * m):
        if b == k:
            return matrix[x][y]
        seen[x][y] = True
        cr = x + dr[di]
        cc = y + dc[di]
        if 0 <= cr < n and 0 <= cc < m and not seen[cr][cc]:
            x = cr
            y = cc
        else:
            di = (di + 1) % 4
            x += dr[di]
            y += dc[di]
        b += 1
"""
QUESTION:
Given a positive integer n that represents dimensions of a 4n x 4n matrix with values from 1 to 4*n*4*n filled from left to right and top to bottom. Your task is to form two coils from matrix and print the coils.
Follow the given examples for better understanding.
 
Example 1:
Input:
n = 1
Output:
10 6 2 3 4 8 12 16
7 11 15 14 13 9 5 1 
Explanation:
The matrix is 
1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16
So, the two coils are as given in the Ouput.
Example 2:
Input:
n = 2
Output:
36 28 20 21 22 30 38 46
54 53 52 51 50 42 34 26
18 10 2 3 4 5 6 7 8
16 24 32 40 48 56 64
29 37 45 44 43 35 27 19
11 12 13 14 15 23 31 39
47 55 63 62 61 60 59 58
57 49 41 33 25 17 9 1  
Explanation:
Your Task:
You don't need to read input or print anything. Your task is to complete the function formCoils() which takes an Integer n as input and returns a vector of two vectors representing coil1 and coil2.
 
Expected Time Complexity: O(n^{2})
Expected Auxiliary Space: O(n^{2})
 
Constraints:
1 <= n <= 20
"""

def form_coils(n):
    ans = [[], []]
    curr = [[4 * n - 1, 4 * n - 1], [0, 0]]
    d0 = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    d1 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    m = [[0 for _ in range(4 * n)] for _ in range(4 * n)]
    start = 1
    for i in range(4 * n):
        for j in range(4 * n):
            m[i][j] = start
            start += 1
    marked = [[0 for _ in range(4 * n)] for _ in range(4 * n)]
    k = 0
    while len(ans[0]) < 8 * n * n:
        marked[curr[0][0]][curr[0][1]] = 1
        ans[0].append(m[curr[0][0]][curr[0][1]])
        marked[curr[1][0]][curr[1][1]] = 1
        ans[1].append(m[curr[1][0]][curr[1][1]])
        if not (curr[0][0] + d0[k][0] < 4 * n and curr[0][0] + d0[k][0] >= 0 and (curr[0][1] + d0[k][1] >= 0) and (curr[0][1] + d0[k][1] < 4 * n) and (marked[curr[0][0] + d0[k][0]][curr[0][1] + d0[k][1]] == 0)):
            k = (k + 1) % 4
        curr[0][0] += d0[k][0]
        curr[0][1] += d0[k][1]
        curr[1][0] += d1[k][0]
        curr[1][1] += d1[k][1]
    ans[0].reverse()
    ans[1].reverse()
    return ans
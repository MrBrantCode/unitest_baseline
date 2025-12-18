"""
QUESTION:
CQXYM found a rectangle A of size n × m. There are n rows and m columns of blocks. Each block of the rectangle is an obsidian block or empty. CQXYM can change an obsidian block to an empty block or an empty block to an obsidian block in one operation.

A rectangle M size of a × b is called a portal if and only if it satisfies the following conditions:

  * a ≥ 5,b ≥ 4. 
  * For all 1 < x < a, blocks M_{x,1} and M_{x,b} are obsidian blocks. 
  * For all 1 < x < b, blocks M_{1,x} and M_{a,x} are obsidian blocks. 
  * For all 1<x<a,1<y<b, block M_{x,y} is an empty block. 
  * M_{1, 1}, M_{1, b}, M_{a, 1}, M_{a, b} can be any type. 

Note that the there must be a rows and b columns, not b rows and a columns.

Note that corners can be any type

CQXYM wants to know the minimum number of operations he needs to make at least one sub-rectangle a portal.

Input

The first line contains an integer t (t ≥ 1), which is the number of test cases.

For each test case, the first line contains two integers n and m (5 ≤ n ≤ 400, 4 ≤ m ≤ 400). 

Then n lines follow, each line contains m characters 0 or 1. If the j-th character of i-th line is 0, block A_{i,j} is an empty block. Otherwise, block A_{i,j} is an obsidian block.

It is guaranteed that the sum of n over all test cases does not exceed 400.

It is guaranteed that the sum of m over all test cases does not exceed 400.

Output

Output t answers, and each answer in a line.

Examples

Input


1
5 4
1000
0000
0110
0000
0001


Output


12


Input


1
9 9
001010001
101110100
000010011
100000001
101010101
110001111
000001111
111100000
000110000


Output


5

Note

In the first test case, the final portal is like this:
    
    
      
    1110  
    1001  
    1001  
    1001  
    0111
"""

def find_min_operations_for_portal(t, test_cases):
    results = []
    
    for case in test_cases:
        N, M, grid = case
        X = [[0] * (M + 1)]
        for row in grid:
            X.append([0] + [int(c) for c in row])
        
        Y = [[0] * (M + 1) for _ in range(N + 1)]
        for i in range(N + 1):
            for j in range(M + 1):
                Y[i][j] = X[i][j]
        
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                X[i][j] += -X[i - 1][j - 1] + X[i][j - 1] + X[i - 1][j]
        
        R = 10 ** 18
        L = []
        for i in range(5, N + 1):
            for j in range(4, M + 1):
                x = i - 4
                y = j - 3
                r = X[i - 1][j - 1] - X[x][j - 1] - X[i - 1][y] + X[x][y]
                rrr = X[i - 1][j] + X[i][j - 1] - X[i - 1][j - 1] - r - (X[x - 1][j] + X[i][y - 1] - X[x - 1][y - 1])
                r2 = rrr - Y[x][j] - Y[i][y] - Y[x][y]
                rr = r + (2 * (i - x + 1 - 2) + 2 * (j - y + 1 - 2)) - r2
                L.append((rr, x, y))
        
        L.sort(key=lambda x: x[0])
        for i in range(min(len(L), 23)):
            (_, x, y) = L[i]
            for i in range(x + 4, N + 1):
                for j in range(y + 3, M + 1):
                    r = X[i - 1][j - 1] - X[x][j - 1] - X[i - 1][y] + X[x][y]
                    rrr = X[i - 1][j] + X[i][j - 1] - X[i - 1][j - 1] - r - (X[x - 1][j] + X[i][y - 1] - X[x - 1][y - 1])
                    r2 = rrr - Y[x][j] - Y[i][y] - Y[x][y]
                    rr = r + (2 * (i - x + 1 - 2) + 2 * (j - y + 1 - 2)) - r2
                    if R > rr:
                        R = rr
        
        results.append(R)
    
    return results
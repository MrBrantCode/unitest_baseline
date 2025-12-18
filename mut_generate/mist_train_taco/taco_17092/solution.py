"""
QUESTION:
You are situated in an N dimensional grid at position (x1,x2,...,xN). The dimensions of the grid are (D1,D2,...DN). In one step, you can walk one step ahead or behind in any one of the N dimensions. (So there are always 2×N possible different moves). In how many ways can you take M steps such that you do not leave the grid at any point? You leave the grid if at any point xi, either xi≤0 or xi>Di. 

Input Format

The first line contains the number of test cases T. T test cases follow. For each test case, the first line contains N and M, the second line contains x1,x2,…,xN and the 3rd line contains D1,D2,…,DN.

Output Format

Output T lines, one corresponding to each test case. Since the answer can be really huge, output it modulo 1000000007.

Constraints

1≤T≤10

1≤N≤10

1≤M≤300

1≤Di≤100

1≤xi≤Di

SAMPLE INPUT
5
1 287
44
78
1 236
25
87
1 122
41
63
1 260
7
64
1 127
3
73

SAMPLE OUTPUT
38753340
587915072
644474045
423479916
320130104
"""

def calculate_ways_to_move(test_cases):
    mod = 1000000007
    
    results = []
    
    for case in test_cases:
        n = case['N']
        m = case['M']
        x = case['x']
        d = case['D']
        
        mat = [[0 for i in range(n + 1)] for j in range(m + 1)]
        
        for i in range(n):
            mat1 = [[0 for j in range(m + 1)] for k in range(d[i] + 1)]
            D = d[i]
            for j in range(1, D + 1):
                mat1[j][0] = 1
            for j in range(1, m + 1):
                for k in range(1, D + 1):
                    mat1[k][j] = 0
                    if k - 1 > 0:
                        mat1[k][j] = (mat1[k][j] + mat1[k - 1][j - 1]) % mod
                    if k + 1 <= D:
                        mat1[k][j] = (mat1[k][j] + mat1[k + 1][j - 1]) % mod
            mat[0][i + 1] = 1
            for j in range(1, m + 1):
                mat[j][i + 1] = mat1[x[i]][j]
        
        comb = [[0 for i in range(m + 1)] for j in range(m + 1)]
        for i in range(0, m + 1):
            comb[i][0] = 1
            comb[i][i] = 1
        for i in range(1, m + 1):
            for j in range(1, i):
                comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % mod
        
        res = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(0, m + 1):
            res[i][1] = mat[i][1]
        for i in range(0, n + 1):
            res[0][i] = 1
        for i in range(2, n + 1):
            for j in range(1, m + 1):
                res[j][i] = 0
                for k in range(0, j + 1):
                    res[j][i] = (res[j][i] + ((comb[j][j - k] * ((res[k][i - 1] * mat[j - k][i]) % mod)) % mod)) % mod
        
        results.append(res[m][n])
    
    return results
"""
QUESTION:
An n × n square matrix is special, if:  it is binary, that is, each cell contains either a 0, or a 1;  the number of ones in each row and column equals 2. 

You are given n and the first m rows of the matrix. Print the number of special n × n matrices, such that the first m rows coincide with the given ones.

As the required value can be rather large, print the remainder after dividing the value by the given number mod.


-----Input-----

The first line of the input contains three integers n, m, mod (2 ≤ n ≤ 500, 0 ≤ m ≤ n, 2 ≤ mod ≤ 10^9). Then m lines follow, each of them contains n characters — the first rows of the required special matrices. Each of these lines contains exactly two characters '1', the rest characters are '0'. Each column of the given m × n table contains at most two numbers one.


-----Output-----

Print the remainder after dividing the required value by number mod.


-----Examples-----
Input
3 1 1000
011

Output
2

Input
4 4 100500
0110
1010
0101
1001

Output
1



-----Note-----

For the first test the required matrices are: 

011

101

110



011

110

101



In the second test the required matrix is already fully given, so the answer is 1.
"""

def count_special_matrices(n, m, mod, first_m_rows):
    g = [2] * n
    for i in range(m):
        t = first_m_rows[i]
        for x, y in enumerate(t):
            if y == '1':
                g[x] -= 1
    
    one = two = 0
    for q in g:
        if q < 0:
            return 0
        if q == 1:
            one += 1
        if q == 2:
            two += 1
    
    mat = [[0] * 600 for _ in range(600)]
    mat[0][0] = 1
    
    for j in range(n + 1):
        for i in range(n + 1):
            if i - 2 >= 0:
                mat[i][j] += i * (i - 1) // 2 * mat[i - 2][j]
            if j - 1 >= 0:
                mat[i][j] += i * j * mat[i][j - 1]
            if j - 2 >= 0:
                mat[i][j] += j * (j - 1) // 2 * mat[i + 2][j - 2]
            mat[i][j] %= mod
    
    return mat[one][two]
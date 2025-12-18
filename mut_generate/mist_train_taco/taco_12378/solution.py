"""
QUESTION:
Vus the Cossack has a field with dimensions n × m, which consists of "0" and "1". He is building an infinite field from this field. He is doing this in this way:

  1. He takes the current field and finds a new inverted field. In other words, the new field will contain "1" only there, where "0" was in the current field, and "0" there, where "1" was.
  2. To the current field, he adds the inverted field to the right. 
  3. To the current field, he adds the inverted field to the bottom. 
  4. To the current field, he adds the current field to the bottom right. 
  5. He repeats it.



For example, if the initial field was:

\begin{matrix} 1 & 0 & \\\ 1 & 1 & \\\ \end{matrix} 

After the first iteration, the field will be like this:

\begin{matrix} 1 & 0 & 0 & 1 \\\ 1 & 1 & 0 & 0 \\\ 0 & 1 & 1 & 0 \\\ 0 & 0 & 1 & 1 \\\ \end{matrix} 

After the second iteration, the field will be like this:

\begin{matrix} 1 & 0 & 0 & 1 & 0 & 1 & 1 & 0 \\\ 1 & 1 & 0 & 0 & 0 & 0 & 1 & 1 \\\ 0 & 1 & 1 & 0 & 1 & 0 & 0 & 1 \\\ 0 & 0 & 1 & 1 & 1 & 1 & 0 & 0 \\\ 0 & 1 & 1 & 0 & 1 & 0 & 0 & 1 \\\ 0 & 0 & 1 & 1 & 1 & 1 & 0 & 0 \\\ 1 & 0 & 0 & 1 & 0 & 1 & 1 & 0 \\\ 1 & 1 & 0& 0 & 0 & 0 & 1 & 1 \\\ \end{matrix} 

And so on...

Let's numerate lines from top to bottom from 1 to infinity, and columns from left to right from 1 to infinity. We call the submatrix (x_1, y_1, x_2, y_2) all numbers that have coordinates (x, y) such that x_1 ≤ x ≤ x_2 and y_1 ≤ y ≤ y_2.

The Cossack needs sometimes to find the sum of all the numbers in submatrices. Since he is pretty busy right now, he is asking you to find the answers!

Input

The first line contains three integers n, m, q (1 ≤ n, m ≤ 1 000, 1 ≤ q ≤ 10^5) — the dimensions of the initial matrix and the number of queries.

Each of the next n lines contains m characters c_{ij} (0 ≤ c_{ij} ≤ 1) — the characters in the matrix.

Each of the next q lines contains four integers x_1, y_1, x_2, y_2 (1 ≤ x_1 ≤ x_2 ≤ 10^9, 1 ≤ y_1 ≤ y_2 ≤ 10^9) — the coordinates of the upper left cell and bottom right cell, between which you need to find the sum of all numbers.

Output

For each query, print the answer.

Examples

Input


2 2 5
10
11
1 1 8 8
2 4 5 6
1 2 7 8
3 3 6 8
5 6 7 8


Output


32
5
25
14
4


Input


2 3 7
100
101
4 12 5 17
5 4 9 4
1 4 13 18
12 1 14 9
3 10 7 18
3 15 12 17
8 6 8 12


Output


6
3
98
13
22
15
3

Note

The first example is explained in the legend.
"""

def calculate_submatrix_sum(n, m, q, matrix, queries):
    def get(a, b):
        if a < 0 or b < 0:
            return 0
        x = a ^ b
        ans = 1
        while x > 0:
            if x % 2 == 1:
                ans *= -1
            x //= 2
        return ans

    mat = [[1 if cell == '1' else -1 for cell in row] for row in matrix]

    row_sums = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(n):
        for j in range(m):
            row_sums[i + 1][j + 1] = row_sums[i][j + 1] + mat[i][j]

    mat_sums = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(n):
        for j in range(m):
            mat_sums[i + 1][j + 1] = mat_sums[i + 1][j] + row_sums[i + 1][j + 1]

    total = mat_sums[n][m]

    def rect_sum(a, b):
        if a == 0 or b == 0:
            return 0
        top_edge = 0
        right_edge = 0
        small = 0
        x = a // n
        x_rem = a % n
        y = b // m
        y_rem = b % m
        big = 0 if x % 2 == 0 or y % 2 == 0 else total
        big *= get(x - 1, y - 1)
        if x % 2 == 1:
            right_edge = mat_sums[n][y_rem]
        right_edge *= get(x - 1, y)
        if y % 2 == 1:
            top_edge = mat_sums[x_rem][m]
        top_edge *= get(x, y - 1)
        small = mat_sums[x_rem][y_rem]
        small *= get(x, y)
        return top_edge + right_edge + small + big

    results = []
    for (x1, y1, x2, y2) in queries:
        ans = rect_sum(x2, y2) - rect_sum(x1 - 1, y2) - rect_sum(x2, y1 - 1) + rect_sum(x1 - 1, y1 - 1)
        ans = ((x2 - x1 + 1) * (y2 - y1 + 1) + ans) // 2
        results.append(ans)

    return results
"""
QUESTION:
You are given n × m table. Each cell of the table is colored white or black. Find the number of non-empty sets of cells such that:

  All cells in a set have the same color.  Every two cells in a set share row or column. 


-----Input-----

The first line of input contains integers n and m (1 ≤ n, m ≤ 50) — the number of rows and the number of columns correspondingly.

The next n lines of input contain descriptions of rows. There are m integers, separated by spaces, in each line. The number equals 0 if the corresponding cell is colored white and equals 1 if the corresponding cell is colored black.


-----Output-----

Output single integer  — the number of non-empty sets from the problem description.


-----Examples-----
Input
1 1
0

Output
1

Input
2 3
1 0 1
0 1 0

Output
8



-----Note-----

In the second example, there are six one-element sets. Additionally, there are two two-element sets, the first one consists of the first and the third cells of the first row, the second one consists of the first and the third cells of the second row. To sum up, there are 8 sets.
"""

def count_valid_sets(n, m, table):
    def r(x):
        return 2 ** x - 1
    
    k = [[0, 0] for _ in range(m)]
    ans = 0
    
    for i in range(n):
        w = 0
        for j in range(m):
            k[j][table[i][j]] += 1
            if table[i][j] == 0:
                w += 1
        ans += r(w) + r(m - w)
    
    for i in range(m):
        if k[i][0] > 1:
            ans += r(k[i][0]) - k[i][0]
        if k[i][1] > 1:
            ans += r(k[i][1]) - k[i][1]
    
    return ans
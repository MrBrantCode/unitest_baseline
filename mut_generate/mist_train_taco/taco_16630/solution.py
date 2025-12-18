"""
QUESTION:
Chef is here with another matrix A having N rows and M columns,  
such that A_{(i,j)} = (i-1)\cdot M+j. 

Chef decided to make this matrix interesting. He performed K operations on the matrix. In each operation, he will choose either a row or column and multiply all values in that row/column with a non-negative integer V.

An operation is of the form  Q, X, V:
- If Q=0: Multiply each element of the X^{th} row with V.
- If Q=1: Multiply each element of the X^{th} column with V.

Find the sum of all values in the matrix after all K operations are done. Since the value can be large, print it modulo 10^{9} + 7.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of multiple lines of input.
- The first line of each test case contains three space-separated integers N, M, and K — the number of rows, columns, and the operations to be done, respectively.
- The next K lines describe the operations. The i^{th} of these K lines contain three space-separated integers Q_{i}, X_{i}, and V_{i}, as mentioned in the statement.

------ Output Format ------ 

For each test case, output on a new line, the sum of all elements of the matrix after performing the operations, modulo 10^{9} + 7.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$1 ≤ N, M ≤ 10^{9}$
$1 ≤ K ≤ 2\cdot 10^{5}$
$0 ≤ Q_{i} ≤ 1$ 
$1 ≤ X ≤ N$ if $Q_{i}=0$
$1 ≤ X ≤ M$ if $Q_{i}=1$ 
$0 ≤ V_{i} ≤ 10^{9}$ 
- The sum of $K$ over all test cases won't exceed $2\cdot 10^{5}$

----- Sample Input 1 ------ 
2
2 2 2
1 2 0
0 1 2
1 3 1
1 2 6
----- Sample Output 1 ------ 
5
16

----- explanation 1 ------ 
Test case $1$ : The initial matrix is $[[1, 2], [3, 4]]$.
- In the first operation, multiply all elements of the second column with $0$. Thus, the matrix becomes $[[1, 0], [3, 0]]$.
- In the second operation, multiply all elements of the first row with $2$. Thus, the matrix becomes $[[2, 0], [3, 0]]$.

The sum of the elements of the updated matrix is $2+3 = 5$.

Test case $2$: The initial matrix is $[[1, 2, 3]]$.
- In the first operation, multiply all elements of the second column with $6$. Thus, the matrix becomes $[[1, 12, 3]]$.

The sum of the elements of the updated matrix is $1+12+3 = 16$.
"""

def calculate_matrix_sum(n, m, k, operations):
    mod = 10**9 + 7

    def calc(i, j):
        first = 0
        if i % 2 == 0:
            first = i // 2 * (i - 1)
        else:
            first = (i - 1) // 2 * i
        second = 0
        if j % 2 == 0:
            second = j // 2 * (j + 1)
        else:
            second = (j + 1) // 2 * j
        return (second - first) % mod

    row = {}
    col = {}

    for q, x, v in operations:
        if q == 0:
            row[x] = row.get(x, 1) * v % mod
        else:
            col[x] = col.get(x, 1) * v % mod

    var = 0
    cons = 0
    sum_matrix = calc(1, n * m)

    for x in col:
        var = (var + col[x] - 1) % mod
        cons += (col[x] - 1) * x % mod
        cons %= mod
        val = (calc(0, n - 1) * m % mod + n * x % mod) % mod
        sum_matrix = (sum_matrix + val * (col[x] - 1) % mod) % mod

    var = var * m % mod

    for x in row:
        rowno = x
        rowc = row[x]
        sumr = calc((rowno - 1) * m + 1, rowno * m) + var * (rowno - 1) % mod + cons
        sumr %= mod
        add = sumr * (rowc - 1) % mod
        sum_matrix = (sum_matrix + add) % mod

    return sum_matrix
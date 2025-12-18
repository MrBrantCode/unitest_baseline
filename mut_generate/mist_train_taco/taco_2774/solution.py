"""
QUESTION:
Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

Dr.D is now fond of matrices. He is particularly interested in Doofish Matrices. A Doofish Matrix of order $N$ is a matrix with $N$ rows (numbered $1$ through $N$) and $N$ columns (numbered $1$ through $N$) such that:
Each element of this matrix is an integer between $1$ and $2N-1$ inclusive.
For each $i$ and $j$ ($1 ≤ i ≤ N$, $1 ≤ j ≤ 2N-1$), the integer $j$ appears in the $i$-th row and/or in the $i$-th column.

Now, for a given $N$, Dr.D is wondering if there is a Doofish Matrix of order $N$. Find such a matrix or determine that it does not exist. If there are multiple solutions, you may find any one.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first and only line of each test case contains a single integer $N$.

------  Output ------
For each test case:
First, print a line containing the string "Hooray" if a Doofish Matrix of order $N$ exists or "Boo" if it does not.
If it exists, print $N$ more lines describing one such matrix. For each valid $i$, the $i$-th of these lines should contain $N$ space-separated integers ― the elements in the $i$-th row.

------  Constraints ------
$1 ≤ T ≤ 2,000$
$1 ≤ N ≤ 2,000$
the sum of $N^{2}$ over all test cases does not exceed $4 \cdot 10^{6}$

------  Subtasks ------
Subtask #1 (29 points): $N$ is a power of $2$

Subtask #2 (71 points): original constraints

----- Sample Input 1 ------ 
2

1

2
----- Sample Output 1 ------ 
Hooray

1

Hooray

3 1

2 3
"""

def generate_doofish_matrix(N):
    if N == 1:
        return "Hooray", [[1]]
    elif N % 2 == 1:
        return "Boo", None
    else:
        l = list(range(1, N))
        mat = [[0] * N for _ in range(N)]
        
        for i in range(1, N):
            mat[0][i] = l[i - 1]
            mat[i][0] = l[i - 1] + N - 1
        
        k = 1
        for i in range(1, N):
            c = (k + 1) % (N - 1)
            mat[i][N - 1] = l[k % (N - 1)]
            mat[N - 1][i] = mat[i][N - 1] + N - 1
            for j in range(i + 1, N - 1):
                mat[i][j] = l[c % (N - 1)]
                mat[j][i] = mat[i][j] + N - 1
                c = (c + 1) % (N - 1)
            k = (k + 2) % (N - 1)
        
        for i in range(N):
            for j in range(N):
                if i == j:
                    mat[i][j] = 2 * N - 1
        
        return "Hooray", mat
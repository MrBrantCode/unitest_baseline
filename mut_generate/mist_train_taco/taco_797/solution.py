"""
QUESTION:
You are given an integer sequence of length N: A_1,A_2,...,A_N. Let us perform Q operations in order. The i-th operation is described by two integers X_i and Y_i. In this operation, we will choose one of the following two actions and perform it:

* Swap the values of A_{X_i} and A_{Y_i}
* Do nothing



There are 2^Q ways to perform these operations. Find the sum of the inversion numbers of the final sequences for all of these ways to perform operations, modulo 10^9+7.

Here, the inversion number of a sequence P_1,P_2,...,P_M is the number of pairs of integers (i,j) such that 1\leq i < j\leq M and P_i > P_j.

Constraints

* 1 \leq N \leq 3000
* 0 \leq Q \leq 3000
* 0 \leq A_i \leq 10^9(1\leq i\leq N)
* 1 \leq X_i,Y_i \leq N(1\leq i\leq Q)
* X_i\neq Y_i(1\leq i\leq Q)
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N Q
A_1
:
A_N
X_1 Y_1
:
X_Q Y_Q


Output

Print the sum of the inversion numbers of the final sequences, modulo 10^9+7.

Examples

Input

3 2
1
2
3
1 2
1 3


Output

6


Input

5 3
3
2
3
1
4
1 5
2 3
4 2


Output

36


Input

9 5
3
1
4
1
5
9
2
6
5
3 5
8 9
7 9
3 2
3 8


Output

425
"""

def calculate_inversion_sum(n, q, A, operations):
    MOD = 10 ** 9 + 7
    INV2 = (MOD + 1) // 2
    
    # Initialize the matrix
    mat = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            mat[i][j] = int(A[i] < A[j])
    
    # Process each operation
    for (x, y) in operations:
        x -= 1
        y -= 1
        mat[x][y] = mat[y][x] = (mat[x][y] + mat[y][x]) * INV2 % MOD
        for i in range(n):
            if i == x or i == y:
                continue
            mat[x][i] = mat[y][i] = (mat[x][i] + mat[y][i]) * INV2 % MOD
            mat[i][x] = mat[i][y] = (mat[i][x] + mat[i][y]) * INV2 % MOD
    
    # Calculate the sum of inversion numbers
    ans = sum((sum(row[:i]) for (i, row) in enumerate(mat))) % MOD
    ans = (ans << q) % MOD
    
    return ans
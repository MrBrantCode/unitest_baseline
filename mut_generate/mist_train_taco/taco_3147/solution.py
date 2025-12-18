"""
QUESTION:
You are given a square matrix M and a positive integer N. You will have to compute M raised to the power N. (that is, M multiplied with itself N times.)

Input

First line of input is T ( number of test-cases) .

First line of each test-case contains two integer M , N where M is size of square array that you have to exponent and N is the power to which you have to exponent .

Next M lines describe the input matrix. Each line contains exactly M elements separated  by single space .

Output

Output M line corresponding to each row of resultant matrix .Each line must have M integers where jth element of ith line is jth element of resultant matrix taken modulo with 1000000007 (10^9+7).

Elements of each row of resultant matrix must be separated by single space.

Conatraints

1 ≤ T ≤ 10

1 ≤ M ≤ 50

1 ≤ N ≤ 100000

0 ≤ element of input matrix ≤ 10^9

SAMPLE INPUT
2
2 3
1 0 
1 1 
3 3
1 0 4 
1 2 2 
0 4 4

SAMPLE OUTPUT
1 0 
3 1 
17 112 116 
15 88 100 
28 144 160
"""

def matrix_exponentiation(M, m, N):
    """
    Computes the matrix M raised to the power N.

    Parameters:
    M (list of lists): The input square matrix.
    m (int): The size of the square matrix (M is an m x m matrix).
    N (int): The exponent to which the matrix M is to be raised.

    Returns:
    list of lists: The resultant matrix after raising M to the power N, with each element modulo 1000000007.
    """
    
    def matrix_mult(A, B, m):
        C = [[0 for _ in range(m)] for _ in range(m)]
        for i in range(m):
            for j in range(m):
                for k in range(m):
                    C[i][k] = (C[i][k] + A[i][j] * B[j][k]) % 1000000007
        return C

    def fast_exponentiation(A, m, n):
        if n == 1:
            return A
        else:
            if n % 2 == 0:
                A1 = fast_exponentiation(A, m, n // 2)
                return matrix_mult(A1, A1, m)
            else:
                A1 = fast_exponentiation(A, m, n - 1)
                return matrix_mult(A, A1, m)

    return fast_exponentiation(M, m, N)
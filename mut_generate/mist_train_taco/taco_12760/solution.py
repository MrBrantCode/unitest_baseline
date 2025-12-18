"""
QUESTION:
You are given <var>Q</var> tuples of integers <var>(L_i, A_i, B_i, M_i)</var>. For each tuple, answer the following question. 
There is an arithmetic progression with L terms: s_0, s_1, s_2, ... , s_{L-1}.
The initial term is A, and the common difference is B. That is, s_i = A + B \times i holds.
Consider the integer obtained by concatenating the terms written in base ten without leading zeros. For example, the sequence 3, 7, 11, 15, 19 would be concatenated into 37111519. What is the remainder when that integer is divided by M?

-----Constraints-----
 - All values in input are integers.
 - 1 \leq L, A, B < 10^{18}
 - 2 \leq M \leq 10^9
 - All terms in the arithmetic progression are less than 10^{18}.

-----Input-----
Input is given from Standard Input in the following format:
L A B M

-----Output-----
Print the remainder when the integer obtained by concatenating the terms is divided by M.

-----Sample Input-----
5 3 4 10007

-----Sample Output-----
5563

Our arithmetic progression is 3, 7, 11, 15, 19, so the answer is 37111519 mod 10007, that is, 5563.
"""

def arithmetic_progression_concat_remainder(L, A, B, M):
    """
    Calculate the remainder when the integer obtained by concatenating the terms of an arithmetic progression
    is divided by M.

    Parameters:
    L (int): The number of terms in the arithmetic progression.
    A (int): The initial term of the arithmetic progression.
    B (int): The common difference of the arithmetic progression.
    M (int): The modulus value to compute the remainder.

    Returns:
    int: The remainder when the concatenated integer is divided by M.
    """
    def mat_mul(X, Y, mod):
        m = len(X)
        return [[sum((X[i][k] * Y[k][j] % mod for k in range(m))) % mod for j in range(m)] for i in range(m)]

    def mat_pow(M, k, mod):
        m = len(M)
        res = [[1 if i == j else 0 for j in range(m)] for i in range(m)]
        while k > 0:
            if k & 1:
                res = mat_mul(M, res, mod)
            M = mat_mul(M, M, mod)
            k >>= 1
        return res

    D = [(0, 0)]
    for d in range(1, 20):
        l = D[-1][1]
        r = max(0, min((10 ** d - 1 - A) // B + 1, L))
        D.append((l, r))

    R = [0, A, 1]
    Mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    for d in range(1, 20):
        num = D[d][1] - D[d][0]
        MM = [[10 ** d, 0, 0], [1, 1, 0], [0, B, 1]]
        Mat = mat_mul(Mat, mat_pow(MM, num, M), M)

    X = sum((R[i] * Mat[i][0] % M for i in range(3))) % M
    return X
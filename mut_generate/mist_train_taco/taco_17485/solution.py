"""
QUESTION:
We all know that every positive integer can be represented as the sum of one or more odd integers. For eg: 4 = 1 + 1 + 1 + 1. Now, your task in this question is to find out the value of G(n), which equals to the number of all possible representations, as described above, of the given integer, n. Since the answer could be very large, you need to output it modulo 1000000007 (10^9 +7).

Note : Order in which the odd integers appear in the representation of n does matter . For eg : Two possible representations of 4 are : 1 + 3 and 3 + 1 are counted individually.

Input :
The first line of the input contains an integer T, the number of test cases. Then T test cases follow. Each test case consists of a line which contains a positive integer, n.

Output :
Output on a new line the value of G(n).

Constraints :
1 ≤ T ≤ 1000 
1 ≤ n ≤10^18

SAMPLE INPUT
2
1
4

SAMPLE OUTPUT
1
3
"""

def calculate_G_of_n(n: int, MOD: int = 1000000007) -> int:
    def mMult(a, b):
        res = [[0, 0], [0, 0]]
        res[1][0] = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % MOD
        res[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % MOD
        res[0][0] = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % MOD
        res[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % MOD
        return res

    def mVec(A, v):
        res = [0, 0]
        res[0] = (A[0][0] * v[0] + A[0][1] * v[1]) % MOD
        res[1] = (A[1][0] * v[0] + A[1][1] * v[1]) % MOD
        return res

    mat = [[1, 1], [1, 0]]
    v = [1, 1]
    n -= 1
    while n > 0:
        if n % 2:
            v = mVec(mat, v)
        mat = mMult(mat, mat)
        n //= 2
    return v[0]
"""
QUESTION:
We all know that every positive integer can be represented as the sum of one or more odd integers. 
For eg: 4 = 1 + 1 + 1 + 1. Now, your task in this question is to find out the value of G(n), which equals to the number of all possible representations, as described above, of the given integer, n.  Since the answer could be very large, you need to output it modulo 1000000007 (10^9 +7). 

Note : Order in which the odd integers appear in the representation of n does matter . For eg : Two possible representations of 4 are :  1 + 3 and 3 + 1 are counted individually.  
Input :
The first line of the input contains an integer T, the number of test cases. Then T test cases follow. Each test case consists of a line which contains a positive integer, n.

Output :
Output on a new line the value of G(n).

Constraints :
1 ≤ T ≤ 1000

1 ≤ n ≤10^18

Warning : large Input/Output data, be careful with certain languages.
SAMPLE INPUT
2
1
4

SAMPLE OUTPUT
1
3
"""

def calculate_G_of_n(n: int, mod: int = 1000000007) -> int:
    fib_matrix = [[1, 1], [1, 0]]

    def matrix_square(A, mod):
        return mat_mult(A, A, mod)

    def mat_mult(A, B, mod):
        return [
            [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod]
        ]

    def matrix_pow(M, power, mod):
        if power <= 0:
            return M

        powers = list(reversed([True if i == "1" else False for i in bin(power)[2:]]))
        matrices = [None for _ in powers]
        matrices[0] = M

        for i in range(1, len(powers)):
            matrices[i] = matrix_square(matrices[i - 1], mod)

        result = None

        for matrix, power in zip(matrices, powers):
            if power:
                if result is None:
                    result = matrix
                else:
                    result = mat_mult(result, matrix, mod)

        return result

    return matrix_pow(fib_matrix, n, mod)[0][1]
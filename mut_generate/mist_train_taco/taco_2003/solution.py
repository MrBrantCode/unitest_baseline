"""
QUESTION:
Amit has been practicing "pattern printing" problems a lot. To test his ability Jitendra gives him a problem.He tells him to print the given matrix in the diagonal fashion.

Note: Direction of the diagonal is from the upper-right corner to lower-left corner.See sample test cases for more clarification.Imagine you are Amit. Write the code to prove your ability!

Input:

First line contain the values of N and M.

Next N lines contain M space separated numbers.

Output:

Print the given matrix in the diagonal fashion as described.

Constraints:

1 ≤ N,M ≤ 100

0 ≤ element of matrix ≤100

SAMPLE INPUT
3 3
1 2 3 
5 6 7
0 1 2

SAMPLE OUTPUT
1 
2 5 
3 6 0 
7 1 
2
"""

def print_matrix_diagonally(matrix, N, M):
    for i in range(N + M - 1):
        j = 0
        while j <= i:
            if i - j < M and i - j >= 0 and j < N:
                print(matrix[j][i - j], end=' ')
            j += 1
        print()
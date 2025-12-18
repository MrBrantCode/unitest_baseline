"""
QUESTION:
Before the start of the football season in Berland a strange magic ritual is held. The most experienced magicians have to find a magic matrix of the size n × n (n is even number). Gods will never allow to start the championship without it. Matrix should contain integers from 0 to n - 1, main diagonal should contain only zeroes and matrix should be symmetric. Moreover, all numbers in each row should be different. Magicians are very tired of the thinking process, so they ask you to write a program to find such matrix.

Input

The first line contains one integer n (2 ≤ n ≤ 1000), n is even.

Output

Output n lines with n numbers each — the required matrix. Separate numbers with spaces. If there are several solutions, output any.

Examples

Input

2


Output

0 1
1 0


Input

4


Output

0 1 3 2
1 0 2 3
3 2 0 1
2 3 1 0
"""

def generate_magic_matrix(n):
    # Initialize the matrix with zeroes
    a = [[0 for j in range(n)] for i in range(n)]
    
    # Fill the matrix according to the given rules
    for i in range(n - 1):
        for j in range(n - 1):
            if i != j:
                a[i][j] = (i + j) % n + int(i + j >= n)
        a[i][n - 1] = ((n - 1 + 2 * i) % n + int(n - 1 + 2 * i >= n)) % n + int(n - 1 + 2 * i > 2 * (n - 1))
    
    for i in range(n - 1):
        a[n - 1][i] = ((n - 1 + 2 * i) % n + int(n - 1 + 2 * i >= n)) % n + int(n - 1 + 2 * i > 2 * (n - 1))
    
    return a
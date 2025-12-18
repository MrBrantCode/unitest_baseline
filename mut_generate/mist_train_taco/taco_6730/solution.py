"""
QUESTION:
Rani has challenged Nandu to generate Splendid Matrices. Splendid matrices are square matrices with dimensions 2^n X 2^n filled in a particular manner. To explain this manner, Rani gives Nandu the matrices for n=1, n=2 and n=3 : 

n=1
1 2
3 4

n=2 (spacing for clarity)
1  2  5  6
3  4  7  8
9  10 13 14
11 12 15 16

n=3 (spacing for clarity)
1  2  5  6  17 18 21 22 
3  4  7  8  19 20 23 24 
9  10 13 14 25 26 29 30 
11 12 15 16 27 28 31 32 
33 34 37 38 49 50 53 54 
35 36 39 40 51 52 55 56 
41 42 45 46 57 58 61 62 
43 44 47 48 59 60 63 64

Given n, please help Nandu in generating the Splendid Matrix with dimensions 2^n X 2^n.
Input
A single line consisting of n.
Output
n lines. Each line should consist of n integers separated by single spaces.
Constraints
1 < = n < = 10

SAMPLE INPUT
3

SAMPLE OUTPUT
1 2 5 6 17 18 21 22 
3 4 7 8 19 20 23 24 
9 10 13 14 25 26 29 30 
11 12 15 16 27 28 31 32 
33 34 37 38 49 50 53 54 
35 36 39 40 51 52 55 56 
41 42 45 46 57 58 61 62 
43 44 47 48 59 60 63 64
"""

def generate_splendid_matrix(n):
    # Initialize a matrix of appropriate size
    matrix = [[0 for _ in range(2**n)] for _ in range(2**n)]
    
    def splendid(n, s, a, b):
        if n > 1:
            p = (2**(n-1)) * (2**(n-1))
            k = (2**n) // 2
            splendid(n-1, s, a, b)
            splendid(n-1, s + p, a, b + k)
            splendid(n-1, s + p * 2, a + k, b)
            splendid(n-1, s + p * 3, a + k, b + k)
        elif n == 1:
            matrix[a][b] = s
            matrix[a][b+1] = s + 1
            matrix[a+1][b] = s + 2
            matrix[a+1][b+1] = s + 3
    
    # Start the recursive generation
    splendid(n, 1, 0, 0)
    
    return matrix
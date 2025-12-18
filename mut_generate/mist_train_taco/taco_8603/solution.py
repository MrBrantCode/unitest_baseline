"""
QUESTION:
The fight between Batman and Superman just got dirty. Superman tried to trick Batman and locked him inside an N x N grid. This gird is really special. It has values at each of its cell which is some positive integer.

Superman gave Batman a serious headache inside the grid. He gave him an integer K and ordered him to tell count of such K x K matrix which when summed equals a perfect cube. Only if Batman gives the correct answer will the grid open and let Batman out.

Batman being not so good at coding turns to you for help. Its time for you to prove that you are a real Batman Fan by helping him out.

Input:

The first line contains 2 integers N and K . This is followed up by an N x N matrix.

Output:

Print number of such K X K matrix whose sum is a perfect cube.

Constraints :

 N  ≤ 1000

 K  ≤ N

All values in matrix  ≤ 10^9

SAMPLE INPUT
3 2
5 69 2 
42 9 9 
5 8 1 

SAMPLE OUTPUT
3

Explanation

The 3:  2x2 matrices whose sum equals a perfect cube are:

(1,1) to (2,2)

(2,1) to (3,2)

(2,2) to (3,3)
"""

def is_perfect_cube(x):
    x = abs(x)
    return int(round(x ** (1. / 3))) ** 3 == x

def count_perfect_cube_submatrices(n, k, matrix):
    # Precompute the sum of each k x 1 column segment
    mat = []
    for i in range(n):
        l = matrix[i]
        sum_val = 0
        prev = l[0]
        for x in l[0:k]:
            sum_val += x
        l[0] = sum_val
        for j in range(1, n-k+1):
            sum_val = sum_val - prev + l[j+k-1]
            prev = l[j]
            l[j] = sum_val
        mat.append(l)
    
    count = 0
    # Check each k x k submatrix
    for i in range(n-k+1):
        c = 0
        for z in range(0, k):
            c += mat[z][i]
        if is_perfect_cube(c):
            count += 1
        for j in range(1, n-k+1):
            c = c - mat[j-1][i] + mat[j+k-1][i]
            if is_perfect_cube(c):
                count += 1
    
    return count
"""
QUESTION:
Let's define logical OR as an operation on two logical values (i. e. values that belong to the set {0, 1}) that is equal to 1 if either or both of the logical values is set to 1, otherwise it is 0. We can define logical OR of three or more logical values in the same manner:

$a_{1} OR a_{2} OR \ldots OR a_{k}$ where $a_{i} \in \{0,1 \}$ is equal to 1 if some a_{i} = 1, otherwise it is equal to 0.

Nam has a matrix A consisting of m rows and n columns. The rows are numbered from 1 to m, columns are numbered from 1 to n. Element at row i (1 ≤ i ≤ m) and column j (1 ≤ j ≤ n) is denoted as A_{ij}. All elements of A are either 0 or 1. From matrix A, Nam creates another matrix B of the same size using formula:

[Image].

(B_{ij} is OR of all elements in row i and column j of matrix A)

Nam gives you matrix B and challenges you to guess matrix A. Although Nam is smart, he could probably make a mistake while calculating matrix B, since size of A can be large.


-----Input-----

The first line contains two integer m and n (1 ≤ m, n ≤ 100), number of rows and number of columns of matrices respectively.

The next m lines each contain n integers separated by spaces describing rows of matrix B (each element of B is either 0 or 1).


-----Output-----

In the first line, print "NO" if Nam has made a mistake when calculating B, otherwise print "YES". If the first line is "YES", then also print m rows consisting of n integers representing matrix A that can produce given matrix B. If there are several solutions print any one.


-----Examples-----
Input
2 2
1 0
0 0

Output
NO

Input
2 3
1 1 1
1 1 1

Output
YES
1 1 1
1 1 1

Input
2 3
0 1 0
1 1 1

Output
YES
0 0 0
0 1 0
"""

def guess_matrix_a(m, n, b):
    # Initialize matrix A with all 1s
    a = [[1 for j in range(n)] for i in range(m)]
    
    # Apply the rules to modify matrix A based on matrix B
    for i in range(m):
        for j in range(n):
            if b[i][j] == 0:
                for k in range(m):
                    a[k][j] = 0
                for k in range(n):
                    a[i][k] = 0
    
    # Create a temporary matrix to check if B can be derived from A
    temp = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        if 1 in a[i]:
            for j in range(n):
                temp[i][j] = 1
    for i in range(n):
        if 1 in [a[j][i] for j in range(m)]:
            for j in range(m):
                temp[j][i] = 1
    
    # Check if the derived matrix matches B
    for i in range(m):
        for j in range(n):
            if b[i][j] != temp[i][j]:
                return "NO", None
    
    # If the derived matrix matches B, return "YES" and the matrix A
    return "YES", a
"""
QUESTION:
You are given four integers: H, W, h and w (1 ≤ h ≤ H, 1 ≤ w ≤ W). Determine whether there exists a matrix such that all of the following conditions are held, and construct one such matrix if the answer is positive:

* The matrix has H rows and W columns.
* Each element of the matrix is an integer between -10^9 and 10^9 (inclusive).
* The sum of all the elements of the matrix is positive.
* The sum of all the elements within every subrectangle with h rows and w columns in the matrix is negative.

Constraints

* 1 ≤ h ≤ H ≤ 500
* 1 ≤ w ≤ W ≤ 500

Input

Input is given from Standard Input in the following format:


H W h w


Output

If there does not exist a matrix that satisfies all of the conditions, print `No`.

Otherwise, print `Yes` in the first line, and print a matrix in the subsequent lines in the following format:


a_{11} ... a_{1W}
:
a_{H1} ... a_{HW}


Here, a_{ij} represents the (i,\ j) element of the matrix.

Examples

Input

3 3 2 2


Output

Yes
1 1 1
1 -4 1
1 1 1


Input

2 4 1 2


Output

No


Input

3 4 2 3


Output

Yes
2 -5 8 7
3 -5 -4 -5
2 1 -1 7
"""

def construct_matrix(H, W, h, w):
    # Initialize the matrix with 1s
    L = [[1] * W for _ in range(H)]
    
    # If the subrectangle dimensions are not 1x1, fill the matrix with a large number
    if h * w != 1:
        x = (10 ** 9 - 1) // (h * w - 1)
        for i in range(H):
            for j in range(W):
                L[i][j] = x
    
    # Set the bottom-right corner of each subrectangle to a large negative number
    for i in range(H // h):
        for j in range(W // w):
            L[(i + 1) * h - 1][(j + 1) * w - 1] = -10 ** 9
    
    # Calculate the sum of all elements in the matrix
    s = sum(sum(row) for row in L)
    
    # If the sum is negative, return 'No'
    if s < 0:
        return ('No', None)
    
    # Otherwise, return 'Yes' and the constructed matrix
    return ('Yes', L)
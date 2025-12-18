"""
QUESTION:
Consider the generalized Fibonacci number G, which is dependent on a, b and c as follows :-
G(1) = 1, G(2) = 1. G(n) = aG(n-1) + bG(n-2) + c.
Your task is to calculate G(n)%m for given values of n and m.
Example 1:
Input:
a = 3, b = 3, c = 3, n = 3, m = 5
Output:
4
Explanation:
G(1) = 1 and G(2) = 1 
G(3) = 3*G(2) + 3*G(1) + 3 = 3*1 + 3*1 + 3 = 9
We need to return answer modulo 5, so 9%5 = 4, is the answer.
Example 2:
Input:
a = 2, b = 2, c = 2, n = 4, m = 100
Output:
16
Explanation:
G(1) = 1 and G(2) = 1 
G(3) = 2*G(2) + 2*G(1) + 2 = 2*1 + 2*1 + 2 = 6
G(4) = 2*G(3) + 2*G(2) + 2  = 2*6 + 2*1 + 2 = 16
We need to return answer modulo 100, so 16%100 = 16, is the answer.
Your Task:
You don't need to read input or print anything. Your task is to complete the function genFibNum() which takes 5 Integers a, b, c, n, and m as input and returns G(n)%m.
Expected Time Complexity: O(logn)
Expected Auxiliary Space: O(1)
Constraints:
1 <= a,b,c,n,m <= 10^{9}+7
"""

def genFibNum(a, b, c, n, m):
    # Initialize the result and transformation matrices
    res = [[0 for _ in range(3)] for _ in range(3)]
    mat = [[0 for _ in range(3)] for _ in range(3)]
    
    # Set up the identity matrix in res
    res[0][0] = res[1][1] = res[2][2] = 1
    
    # Set up the transformation matrix mat
    mat[0][0] = a
    mat[0][1] = b
    mat[0][2] = mat[1][0] = mat[2][2] = 1
    mat[1][1] = mat[1][2] = mat[2][0] = mat[2][1] = 0
    
    # If n is 1 or 2, return 1 % m
    if n <= 2:
        return 1 % m
    
    # Function to multiply two matrices under modulo m
    def mul(res, mat, m):
        res1 = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    res1[i][j] += res[i][k] * mat[k][j]
                    res1[i][j] %= m
        for i in range(3):
            for j in range(3):
                res[i][j] = res1[i][j]
    
    # Function to exponentiate the matrix under modulo m
    def mat_exp(n, m):
        while n > 0:
            if n & 1:
                mul(res, mat, m)
            mul(mat, mat, m)
            n //= 2
    
    # Exponentiate the matrix to compute the result
    mat_exp(n - 2, m)
    
    # Compute the final result
    return (res[0][0] + res[0][1] + c * res[0][2]) % m
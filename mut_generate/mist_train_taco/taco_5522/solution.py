"""
QUESTION:
Given a sequence as follow:
1,1,7,19,73....
Find the N^{th} term of the given sequence.
 
Example 1:
Input: N = 1
Output: 1
Example 2:
Input: N = 4
Output: 19
 
Your Task:
Your task is to complete the function NthTerm() which takes N as input paramater and returns N^{th} term of the given sequence modulo 10^{9}+7.
 
Expected Time Complexity: O(log(N))
Expected Space Compelxity: O(K) where K is constant.
 
Constraints:
1 <= N <= 10^{10}
"""

def find_nth_term(n: int) -> int:
    MODULO = 10**9 + 7
    
    def matrix_2x2_multiplication(A, B):
        [[a11, a12], [a21, a22]] = A
        [[b11, b12], [b21, b22]] = B
        return [
            [(a11 * b11 + a12 * b21) % MODULO, (a11 * b12 + a12 * b22) % MODULO],
            [(a21 * b11 + a22 * b21) % MODULO, (a21 * b12 + a22 * b22) % MODULO]
        ]
    
    ID_2x2 = [[1, 0], [0, 1]]
    
    def matrix_2x2_power(A, n):
        if n == 0:
            return ID_2x2
        if n == 1:
            return A
        X = A
        Y = ID_2x2
        m = n
        while m > 1:
            if m & 1:
                Y = matrix_2x2_multiplication(Y, X)
            X = matrix_2x2_multiplication(X, X)
            m >>= 1
        Y = matrix_2x2_multiplication(Y, X)
        return Y
    
    SEQ = [[2, 5], [1, 0]]
    
    if n <= 0:
        return 0
    elif n < 3:
        return 1
    else:
        A = matrix_2x2_power(SEQ, n - 2)
        return (A[0][0] + A[0][1]) % MODULO
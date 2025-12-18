"""
QUESTION:
Create a function named `operation_matrix` that takes two inputs, `M` and `N`, where `M` is a positive integer and `N` is a string representing a mathematical operation (+, -, *, /). The function should return a 2D matrix of size `(M+1) x (M+1)` where the element at the p-th row and q-th column is the result of the operation `N` applied to `p` and `q`. If `N` is not one of the four basic arithmetic operations, the function should return "Invalid operation". If `N` is '/' and `q` is 0, the element at the p-th row and q-th column should be 'Undefined'.
"""

def operation_matrix(M, N):
    ops = {
        '+': lambda p, q: p + q,
        '-': lambda p, q: p - q,
        '*': lambda p, q: p * q,
        '/': lambda p, q: p / q if q != 0 else 'Undefined',
    }
    
    if N not in ops.keys():
        return "Invalid operation"
    
    return [[ops[N](p, q) for q in range(M+1)] for p in range(M+1)]
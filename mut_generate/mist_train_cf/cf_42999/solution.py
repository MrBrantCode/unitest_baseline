"""
QUESTION:
Write a function `max_expression_value` that calculates the maximum value of the expression `(A[i] - B[j])^2 + (A[i] - X)^2 + (B[j] - Y)^2` given two arrays `A` and `B` each containing `N` integers and two constants `X` and `Y`. The function should take in parameters `N`, `X`, `Y`, `A`, and `B` where `N` is an integer between 1 and 1000, `X` and `Y` are integers between 1 and 1000, and `A` and `B` are lists of `N` integers between -1000 and 1000.
"""

def max_expression_value(N, X, Y, A, B):
    max_val = float('-inf')
    for i in range(N):
        for j in range(N):
            expression_val = (A[i] - B[j])**2 + (A[i] - X)**2 + (B[j] - Y)**2
            max_val = max(max_val, expression_val)
    return max_val
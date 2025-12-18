"""
QUESTION:
Write a function `catalan(n)` that calculates the nth Catalan number using memoization. The function should take a non-negative integer `n` as input and return the corresponding Catalan number. If `n` is not a non-negative integer, the function should return an error message.
"""

def catalan(n, catalan_dict={0: 1, 1: 1}):
    if type(n) != int or n < 0:
        return "Error: Please enter a non-negative integer."

    if n in catalan_dict:
        return catalan_dict[n]
    else:
        catalan_dict[n] = 2 * (2*n - 1) * catalan(n-1) // (n+1)
        return catalan_dict[n]
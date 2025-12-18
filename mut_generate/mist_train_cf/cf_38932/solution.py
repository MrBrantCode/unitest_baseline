"""
QUESTION:
Implement a function `fermatsFactorBasic(N)` that takes an integer `N` as input and returns a tuple of two integers representing the factors of `N` using Fermat's factorization method. The function should use the `Decimal` class to handle the square root calculation and implement the remaining steps of Fermat's factorization method to find the factors. Assume `N` is an odd integer.
"""

from decimal import Decimal, ROUND_CEILING

def entrance(N):  
    NN = Decimal(N)
    A = NN.sqrt()    
    A = A.to_integral_value(rounding=ROUND_CEILING)
    
    while True:
        B2 = A * A - NN
        B = B2.sqrt()
        if B * B == B2:
            factor1 = int(A - B)
            factor2 = int(A + B)
            return (factor1, factor2)
        A += 1
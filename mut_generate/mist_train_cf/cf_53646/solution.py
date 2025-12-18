"""
QUESTION:
Write a function main(n) that takes an integer n as input and returns the total number of tours across a 4 x n game board, where the tour starts at the top left corner and ends at the bottom left corner, modulo 10^8. The tour can move up, down, left, or right by one square, visiting each square precisely once.
"""

import numpy as np

m = 100000000

mat = [ [0]*5 for _ in range(5) ]
mat[0] = [6,2,4,2,1]

for i in range(1,5):
    mat[i][i-1] = 1

def mul(A, B):
    C = [ [0]*5 for _ in range(5) ]
    for i in range(5):
        for j in range(5):
            for k in range(5):
                C[i][j] = (C[i][j]+ A[i][k]*B[k][j]) % m
    return C

def pow_(A, n):
    if n==1:
        return A
    T = pow_(A, n//2)
    if n%2==0:
        return mul(T,T)
    return mul(mul(T,T),A)

def entrance(n):
    if n<5:
        return [1, 2, 4, 8, 16][n]
    else:
        return pow_(mat, n-4)[0][0]
"""
QUESTION:
Write a function `calculateSum` that takes a positive integer N as input and returns the sum of all natural numbers from 1 to N using recursion. The function should only return the sum and not perform any additional operations. The input integer N will always be a positive integer.
"""

def calculateSum(N):
    if N == 1:
        return 1
    else:
        return N + calculateSum(N-1)
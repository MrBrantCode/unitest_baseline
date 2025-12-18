"""
QUESTION:
Given two positive integers `n` and `k`, compute the expected value `E(n, k)` of the sum of squares of black balls extracted over `n` turns, where in each turn `k` black balls are added to an urn initially filled with `kn` white balls, followed by the removal of `2k` balls chosen at random. Implement a function `blackBallExpectedValue` that takes `n` as input and returns the expected value `E(n, 10)` rounded to the nearest integer.
"""

import math

def blackBallExpectedValue(n):
    e, l = [0 for i in range(n)], [0 for i in range(n)]
    l[0], e[0] = 20, 20
    for i in range(1, n):
        a = l[i-1]*((6*i - 1) * 2 - l[i-1])
        b = 20*(6*i*2)
        c = (a + b*20) / ((6*i - 1) * 12 * i)
        l[i] = b + c
        e[i] = e[i - 1] + l[i]
    return round(e[-1])   # round-off to nearest integer
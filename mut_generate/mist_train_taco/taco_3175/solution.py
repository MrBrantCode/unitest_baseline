"""
QUESTION:
In an infinite array with two rows, the numbers in the top row are denoted

`. . . , A[−2], A[−1], A[0], A[1], A[2], . . .`

and the numbers in the bottom row are denoted

`. . . , B[−2], B[−1], B[0], B[1], B[2], . . .`

For each integer `k`, the entry `A[k]` is directly above
the entry `B[k]` in the array, as shown:


...|A[-2]|A[-1]|A[0]|A[1]|A[2]|...
...|B[-2]|B[-1]|B[0]|B[1]|B[2]|...



For each integer `k`, `A[k]` is the average of the entry to its left, the entry to its right,
and the entry below it; similarly, each entry `B[k]` is the average of the entry to its
left, the entry to its right, and the entry above it.


Given `A[0], A[1], A[2] and A[3]`, determine the value of `A[n]`. (Where range of n is -1000 Inputs and Outputs in BigInt!** 

Adapted from 2018 Euclid Mathematics Contest.
https://www.cemc.uwaterloo.ca/contests/past_contests/2018/2018EuclidContest.pdf
"""

def calculate_a_n(A0, A1, A2, A3, n):
    if n < 0:
        return calculate_a_n(A3, A2, A1, A0, 3 - n)
    if n < 4:
        return [A0, A1, A2, A3][n]
    
    a, b, c, d = A0, A1, A2, A3
    for _ in range(n - 3):
        a, b, c, d = b, c, d, 6 * d - 10 * c + 6 * b - a
    
    return d
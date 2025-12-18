"""
QUESTION:
You are given a grid of size M x N, where each square is colored with some random color among K colors with each having equal probability.

A Good Rectangle is defined as one where all squares lying on the inner border are of the same color.

What is the expected number of Good Rectangles in the given grid.

-----Input-----

- 
First Line contains M, N, K

-----Output-----
A single value rounded off to the nearest Integer corresponding to the required answer.

-----Constraints-----
-  1 <= N <= 105 
-  1 <= M <= 105 
-  1 <= K <= 105 

-----Example-----
Input:
1 3 1
Output:
6
"""

def for1(M, k):
    ret = 0.0
    x = k * k + 0.0
    z = x
    for m in range(1, M):
        ret += (M - m) / x
        x *= z
    return ret

def for2(M, k):
    ret = 0.0
    x = k + 0.0
    for m in range(1, M):
        ret += (M - m) / x
        x *= k
    return ret

def calculate_expected_good_rectangles(M, N, K):
    return int(round(M * N + M * for2(N, K) + N * for2(M, K) + K * for1(M, K) * for1(N, K), 0))
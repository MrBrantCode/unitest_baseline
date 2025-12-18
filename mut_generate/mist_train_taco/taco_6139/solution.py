"""
QUESTION:
In Finite Encyclopedia of Integer Sequences (FEIS), all integer sequences of lengths between 1 and N (inclusive) consisting of integers between 1 and K (inclusive) are listed.
Let the total number of sequences listed in FEIS be X. Among those sequences, find the (X/2)-th (rounded up to the nearest integer) lexicographically smallest one.

-----Constraints-----
 - 1 \leq N,K \leq 3 × 10^5
 - N and K are integers.

-----Input-----
Input is given from Standard Input in the following format:
K N

-----Output-----
Print the (X/2)-th (rounded up to the nearest integer) lexicographically smallest sequence listed in FEIS, with spaces in between, where X is the total number of sequences listed in FEIS.

-----Sample Input-----
3 2

-----Sample Output-----
2 1 

There are 12 sequences listed in FEIS: (1),(1,1),(1,2),(1,3),(2),(2,1),(2,2),(2,3),(3),(3,1),(3,2),(3,3).
The (12/2 = 6)-th lexicographically smallest one among them is (2,1).
"""

import math

def find_median_sequence(K, N):
    r = []
    if K == 1:
        r = [1] * ((N + 1) // 2)
    elif K % 2 == 0:
        r = [K // 2]
        r += [K] * (N - 1)
    else:
        t = N // 2
        x = int(math.log(N * (K - 1) + 1, K) - 1)
        while t < ((K ** (x + 1) - 1) / (K - 1) + x) // 2:
            x -= 1
        x += 1
        r = [(K + 1) // 2] * (N - x)
        r += [0] * x
        t = ((K ** (x + 1) - 1) / (K - 1) + x) // 2 - t
        for i in range(x, 0, -1):
            r[N - i] = 1
            t -= 1
            for j in range(K - 1):
                if t == 0:
                    break
                if K ** i - 1 <= t * (K - 1):
                    r[N - i] += 1
                    t -= (K ** i - 1) // (K - 1)
            if t == 0:
                break
        for i in range(len(r) - 1, -1, -1):
            if r[i] == 0:
                r.pop()
            else:
                break
    return r
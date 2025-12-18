"""
QUESTION:
We have an integer sequence A of length N, where A_1 = X, A_{i+1} = A_i + D (1 \leq  i < N ) holds.
Takahashi will take some (possibly all or none) of the elements in this sequence, and Aoki will take all of the others.
Let S and T be the sum of the numbers taken by Takahashi and Aoki, respectively. How many possible values of S - T are there?

-----Constraints-----
 - -10^8 \leq X, D \leq 10^8
 - 1 \leq N \leq 2 \times 10^5
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N X D

-----Output-----
Print the number of possible values of S - T.

-----Sample Input-----
3 4 2

-----Sample Output-----
8

A is (4, 6, 8).
There are eight ways for (Takahashi, Aoki) to take the elements: ((), (4, 6, 8)), ((4), (6, 8)), ((6), (4, 8)), ((8), (4, 6))), ((4, 6), (8))), ((4, 8), (6))), ((6, 8), (4))), and ((4, 6, 8), ()).
The values of S - T in these ways are -18, -10, -6, -2, 2, 6, 10, and 18, respectively, so there are eight possible values of S - T.
"""

def count_possible_differences(N, X, D):
    if D == 0:
        if X == 0:
            return 1
        else:
            return N + 1
    
    if D < 0:
        X *= -1
        D *= -1
    
    p = dict()
    q = dict()
    
    for k in range(N + 1):
        temp = k * X % D
        if temp in p.keys():
            a = (k - p[temp]) * X // D
            L = (k - 1) * k // 2 + a
            H = (2 * N - k - 1) * k // 2 + a
            q[temp].append([L, H])
        else:
            p[temp] = k
            L = (k - 1) * k // 2
            H = (2 * N - k - 1) * k // 2
            q[temp] = [[L, H]]
    
    ans = 0
    for z in q.values():
        c = -float('inf')
        for (a, b) in sorted(z):
            if a > c:
                ans += b - a + 1
            elif b > c:
                ans += b - c
            else:
                continue
            c = b
    
    return ans
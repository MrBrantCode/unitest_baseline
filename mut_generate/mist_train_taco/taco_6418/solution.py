"""
QUESTION:
Read problems statements in Mandarin Chinese  and Russian. 

Little Elephant from Zoo of Lviv has n (0-based numeration) blocks consisted of 1x1x1 cubes in such way that the size of i-th block is 1x1xA_{i}. Each of the blocks also has a color, which is a positive integer. The color of i-th block is C_{i}. There will be no more than two blocks of the same color.

Little Elephant wants to stack the blocks in the stack. In order to do so, he choose some random permutation P of integers from 0 to n-1, inclusive, and stacks all the blocks in order of P, i. e. at first he stacks P_{0}-th block, then P_{1}-th and so on.

After stacking Little Elephant has a sequence of size S consisted of cubes (0-based numeration) in order from the stack, where S = A_{0} + A_{1} + ... + A_{n-1}. Then he counts the number of such pairs of cubes with indices i and j that j - i = k and i-th cube has same color as j-th. Call this number as colorfulness of the corresponding permutation.

Help Little Elephant and for a given n, k and the description of blocks find the expected colorfulness, considering that permutation P is chosen randomly.
 
------ Input ------ 

First line of the input contains single integer T - the number of test cases. Then T test cases follow. First line of each test case contains pair of integers n and k. Next n lines of each test case contain pairs of integers A_{i} and C_{i}.

------ Output ------ 

In T lines print T numbers - the answers for the corresponding test cases. Your answer will considered correct if it has at most 10^{-6} absolute or relative error.

------ Constraints ------ 

1 ≤ T ≤ 10

1 ≤ n ≤ 20

1 ≤ k ≤ 200

1 ≤ A_{i} ≤ 10

1 ≤ C_{i} ≤ n

There will be no three or more blocks of the same color in a single test case.

------ Example ------ 

Input:
1
7 5
3 1
2 2
2 1
4 3
1 2
1 3
4 4

Output:
0.9095238
"""

def calculate_expected_colorfulness(n, k, blocks):
    def Choose(i, s, x, y, cnt):
        if s < 0:
            return 0
        if s == 0:
            return F[cnt] * 2 * F[N - cnt - 2] * (N - cnt - 1)
        if i == N:
            return 0
        if i == x or i == y:
            return Choose(i + 1, s, x, y, cnt)
        if (i, s, x, y, cnt) in Mem:
            return Mem[i, s, x, y, cnt]
        ans = Choose(i + 1, s - A[i], x, y, cnt + 1) + Choose(i + 1, s, x, y, cnt)
        Mem[i, s, x, y, cnt] = ans
        return ans

    F = [1, 1]
    for i in range(2, 21):
        F.append(F[-1] * i)

    Mem = {}
    ans = 0
    N = n
    A = [block[0] for block in blocks]
    C = [block[1] for block in blocks]

    for i in range(N):
        if A[i] > k:
            ans += A[i] - k

    P = []
    for i in range(N):
        for j in range(i + 1, N):
            if C[i] == C[j]:
                P.append((i, j))

    for p in P:
        x = p[0]
        y = p[1]
        Lx = A[x]
        Ly = A[y]
        for j in range(0, k):
            e = Choose(0, j, x, y, 0)
            f = Lx + Ly + j - k
            if j + Ly > k:
                f -= j + Ly - k
            if j + Lx > k:
                f -= j + Lx - k
            if f > 0:
                ans += f * (e / F[N])

    return ans
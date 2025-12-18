"""
QUESTION:
Tim is visiting his grandma for two days and is bored due to the lack of the electricity over there. That's why he starts to play with grandma's colorful candle collection.

He aligned the $N$ candles from left to right. The $\boldsymbol{i}$th candle from the left has the height $\boldsymbol{H}_i$ and the color $C_i$, an integer ranged from 1 to a given $\mbox{K}$, the number of colors. 

Now he stares at the sequence of candles and wonders, how many strictly increasing ( in height ) colorful subsequences are there? A subsequence is considered as colorful if every of the $\mbox{K}$ colors appears at least one times in the subsequence. 

As the number of subsequences fulfilling the requirement can be large, print the result modulo $10^9+7$.

Input Format

On the first line you will be given $N$ and $\mbox{K}$, then $N$ lines will follow. On the $\boldsymbol{i}$th line you will be given two integers $\boldsymbol{H}_i$ and $C_i$. 

Constraints

$1\leq N\leq5\cdot10^4$
$1\leq C_i\leq K\leq7$
$1\leq H_i\leq5\cdot10^4$

Output Format

Print the number of strictly increasing colorful subsequences modulo $10^9+7$. 

Sample Input
4 3
1 1
3 2
2 2
4 3

Sample Output
2

Explanation

In the first sample the only two valid subsequences are (1, 2, 4) and (1, 3, 4).
"""

def count_strictly_increasing_colorful_subsequences(N, K, A):
    def read(T, i):
        s = 0
        while i > 0:
            s += T[i]
            s %= 1000000007
            i -= i & -i
        return s

    def update(T, i, v):
        while i <= 50010:
            T[i] += v
            T[i] %= 1000000007
            i += i & -i
        return v

    def count_bits(b):
        c = 0
        while b:
            b &= b - 1
            c += 1
        return c

    L = 2 ** K
    R = 0
    for i in range(L):
        T = [0 for _ in range(50010)]
        t = 0
        for j in range(N):
            (h, c) = A[j]
            if i >> c - 1 & 1:
                t += update(T, h, read(T, h - 1) + 1)
                t %= 1000000007
        if count_bits(i) % 2 == K % 2:
            R += t
            R %= 1000000007
        else:
            R += 1000000007 - t
            R %= 1000000007
    return R
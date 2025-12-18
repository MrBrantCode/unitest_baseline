"""
QUESTION:
We have N colored balls arranged in a row from left to right; the color of the i-th ball from the left is c_i.
You are given Q queries. The i-th query is as follows: how many different colors do the l_i-th through r_i-th balls from the left have?

-----Constraints-----
 - 1\leq N,Q \leq 5 \times 10^5
 - 1\leq c_i \leq N
 - 1\leq l_i \leq r_i \leq N
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N Q
c_1 c_2 \cdots c_N
l_1 r_1
l_2 r_2
:
l_Q r_Q

-----Output-----
Print Q lines. The i-th line should contain the response to the i-th query.

-----Sample Input-----
4 3
1 2 1 3
1 3
2 4
3 3

-----Sample Output-----
2
3
1

 - The 1-st, 2-nd, and 3-rd balls from the left have the colors 1, 2, and 1 - two different colors.
 - The 2-st, 3-rd, and 4-th balls from the left have the colors 2, 1, and 3 - three different colors.
 - The 3-rd ball from the left has the color 1 - just one color.
"""

def count_distinct_colors(N, Q, C, queries):
    def BIT_query(BIT, idx):
        res_sum = 0
        if idx == 0:
            return 0
        while idx > 0:
            res_sum += BIT[idx]
            idx -= idx & -idx
        return res_sum

    def BIT_update(BIT, idx, x, n):
        while idx <= n:
            BIT[idx] += x
            idx += idx & -idx
        return

    LRI = [(r, l, i) for i, (l, r) in enumerate(queries)]
    LRI.sort(key=lambda x: x[0])
    lastAppend = [-1] * (N + 1)
    BIT = [0] * (N + 1)
    ANS = [0] * Q
    now = 1

    for (r, l, i) in LRI:
        while now <= r:
            c = C[now - 1]
            if lastAppend[c] == -1:
                BIT_update(BIT, now, 1, N)
            else:
                BIT_update(BIT, now, 1, N)
                BIT_update(BIT, lastAppend[c], -1, N)
            lastAppend[c] = now
            now += 1
        ANS[i] = BIT_query(BIT, r) - BIT_query(BIT, l - 1)

    return ANS
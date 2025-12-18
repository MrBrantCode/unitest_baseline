"""
QUESTION:
Fatland is a town that started with N distinct empires, namely empires 1, 2, ..., N. But over time, the armies of some of these empires have taken over other ones. Each takeover occurred when the army of empire i invaded empire j. After each invasion, all of empire j became part of empire i, and empire j was renamed as empire i. 

Empire Huang, leader of Badland, wants to invade Fatland. To do this, he needs to calculate how many distinct empires still remain in Fatland after all the takeovers. Help him with this task.

Input:

The first line contains an integer N, the number of empires that were originally in Fatland.

The second line contains an integer K, denoting the number of takeovers that took place.

Each of the next K lines contains 2 space-separated integers i, j, representing that the army of empire i took over that of empire j. As a result, empire j does not exist anymore and is now renamed as empire i. It is guaranteed that empire i still exists.

Output: Output one integer, the number of empires that exist in Fatland.

Constraints:

1 ≤ N ≤ 10^5

1 ≤ K ≤ 10^5

SAMPLE INPUT
4
2
1 2
4 1

SAMPLE OUTPUT
2

Explanation

Fatland started with empires 1, 2, 3, 4. First, empire 1 invaded empire 2, so empire 2 was renamed to empire 1. Then, empire 4 invaded empire 1. So what were at the beginning empires 1 and 2 were renamed to empire 4. Now, only empires 3 and 4 remain, so the answer is 2.
"""

def count_distinct_empires(N, K, takeovers):
    fa = [i for i in range(N + 1)]

    def findfa(x):
        if x == fa[x]:
            return x
        else:
            fa[x] = findfa(fa[x])
            return fa[x]

    for i, j in takeovers:
        fi, fj = findfa(i), findfa(j)
        if fi != fj:
            fa[fj] = fi

    ans = 0
    for i in range(1, N + 1):
        if i == findfa(i):
            ans += 1

    return ans
"""
QUESTION:
There are N balls in a row. Initially, the i-th ball from the left has the integer A_i written on it.

When Snuke cast a spell, the following happens:

* Let the current number of balls be k. All the balls with k written on them disappear at the same time.



Snuke's objective is to vanish all the balls by casting the spell some number of times. This may not be possible as it is. If that is the case, he would like to modify the integers on the minimum number of balls to make his objective achievable.

By the way, the integers on these balls sometimes change by themselves. There will be M such changes. In the j-th change, the integer on the X_j-th ball from the left will change into Y_j.

After each change, find the minimum number of modifications of integers on the balls Snuke needs to make if he wishes to achieve his objective before the next change occurs. We will assume that he is quick enough in modifying integers. Here, note that he does not actually perform those necessary modifications and leaves them as they are.

Constraints

* 1 \leq N \leq 200000
* 1 \leq M \leq 200000
* 1 \leq A_i \leq N
* 1 \leq X_j \leq N
* 1 \leq Y_j \leq N

Input

Input is given from Standard Input in the following format:


N M
A_1 A_2 ... A_N
X_1 Y_1
X_2 Y_2
:
X_M Y_M


Output

Print M lines. The j-th line should contain the minimum necessary number of modifications of integers on the balls to make Snuke's objective achievable.

Examples

Input

5 3
1 1 3 4 5
1 2
2 5
5 4


Output

0
1
1


Input

4 4
4 4 4 4
4 1
3 1
1 1
2 1


Output

0
1
2
3


Input

10 10
8 7 2 9 10 6 6 5 5 4
8 1
6 3
6 2
7 10
9 7
9 9
2 4
8 1
1 8
7 7


Output

1
0
1
2
2
3
3
3
3
2
"""

from collections import Counter

def min_modifications_to_vanish_balls(N, M, A, changes):
    ac_ = Counter(A)
    ac = {i: ac_[i] if i in ac_ else 0 for i in range(1, N + 1)}
    ad = [0] * N
    
    for (a, c) in ac.items():
        for i in range(max(0, a - c), a):
            ad[i] += 1
    
    ans = ad.count(0)
    anss = []
    
    for (x, y) in changes:
        ax = A[x - 1]
        xdi = ax - ac[ax]
        if xdi >= 0:
            ad[xdi] -= 1
            if ad[xdi] == 0:
                ans += 1
        ac[ax] -= 1
        ac[y] += 1
        ydi = y - ac[y]
        if ydi >= 0:
            ad[ydi] += 1
            if ad[ydi] == 1:
                ans -= 1
        A[x - 1] = y
        anss.append(ans)
    
    return anss
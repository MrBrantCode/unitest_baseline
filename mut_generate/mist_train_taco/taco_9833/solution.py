"""
QUESTION:
Snuke got an integer sequence from his mother, as a birthday present. The sequence has N elements, and the i-th of them is i. Snuke performs the following Q operations on this sequence. The i-th operation, described by a parameter q_i, is as follows:

* Take the first q_i elements from the sequence obtained by concatenating infinitely many copy of the current sequence, then replace the current sequence with those q_i elements.



After these Q operations, find how many times each of the integers 1 through N appears in the final sequence.

Constraints

* 1 ≦ N ≦ 10^5
* 0 ≦ Q ≦ 10^5
* 1 ≦ q_i ≦ 10^{18}
* All input values are integers.

Input

The input is given from Standard Input in the following format:


N Q
q_1
:
q_Q


Output

Print N lines. The i-th line (1 ≦ i ≦ N) should contain the number of times integer i appears in the final sequence after the Q operations.

Examples

Input

5 3
6
4
11


Output

3
3
3
2
0


Input

10 10
9
13
18
8
10
10
9
19
22
27


Output

7
4
4
3
3
2
2
2
0
0
"""

import bisect

def count_final_sequence_occurrences(N, Q, operations):
    que = [(N, 0)]
    for i in range(Q):
        q = operations[i]
        que.append((q, i + 1))
    que.sort(reverse=True)
    
    ext = []
    while que:
        (q, id) = que.pop()
        if not ext:
            ext.append((q, id))
        elif ext[-1][1] < id:
            if ext[-1][0] == q:
                ext.pop()
            ext.append((q, id))
    
    Q = len(ext)
    data = [1] * Q
    data[0] = ext[0][0]
    edge = [[] for i in range(Q)]
    nowext = [ext[0][0]]
    
    for i in range(1, Q):
        q = ext[i][0]
        rest = q
        while True:
            id = bisect.bisect_right(nowext, rest)
            if id == 0:
                break
            else:
                edge[id - 1].append((i, rest // nowext[id - 1]))
                rest %= nowext[id - 1]
        nowext.append(ext[i][0])
        data[i] = rest
    
    dp = [1] * Q
    for i in range(Q - 2, -1, -1):
        temp = 0
        for (nv, c) in edge[i]:
            temp += dp[nv] * c
        dp[i] = temp
    
    minus = [0] * (ext[0][0] + 1)
    for i in range(Q):
        minus[data[i]] += dp[i]
    
    base = sum(dp)
    result = []
    for i in range(1, N + 1):
        if i - 1 <= ext[0][0]:
            base -= minus[i - 1]
        result.append(base)
    
    return result
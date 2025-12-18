"""
QUESTION:
You are given an array $a$ consisting of $n$ integers. In one move, you can jump from the position $i$ to the position $i - a_i$ (if $1 \le i - a_i$) or to the position $i + a_i$ (if $i + a_i \le n$).

For each position $i$ from $1$ to $n$ you want to know the minimum the number of moves required to reach any position $j$ such that $a_j$ has the opposite parity from $a_i$ (i.e. if $a_i$ is odd then $a_j$ has to be even and vice versa).


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 2 \cdot 10^5$) — the number of elements in $a$.

The second line of the input contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le n$), where $a_i$ is the $i$-th element of $a$.


-----Output-----

Print $n$ integers $d_1, d_2, \dots, d_n$, where $d_i$ is the minimum the number of moves required to reach any position $j$ such that $a_j$ has the opposite parity from $a_i$ (i.e. if $a_i$ is odd then $a_j$ has to be even and vice versa) or -1 if it is impossible to reach such a position.


-----Example-----
Input
10
4 5 7 6 7 5 4 4 6 4

Output
1 1 1 2 -1 1 1 3 1 1
"""

from collections import defaultdict, deque

def min_moves_to_opposite_parity(n, arr):
    d = [-1] * n
    parity = [x % 2 for x in arr]
    done = deque()
    lrs = defaultdict(list)
    
    for i in range(n):
        put = False
        if i - arr[i] >= 0:
            if parity[i] != parity[i - arr[i]]:
                d[i] = 1
                done.append(i)
                put = True
            lrs[i - arr[i]].append(i)
        if i + arr[i] < n:
            if not put and parity[i] != parity[i + arr[i]]:
                d[i] = 1
                done.append(i)
            lrs[i + arr[i]].append(i)
    
    while done:
        i = done.popleft()
        for j in lrs[i]:
            if d[j] == -1:
                d[j] = d[i] + 1
                done.append(j)
    
    return d
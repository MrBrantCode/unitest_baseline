"""
QUESTION:
There are some rabbits in Singapore Zoo. To feed them, Zookeeper bought $n$ carrots with lengths $a_1, a_2, a_3, \ldots, a_n$. However, rabbits are very fertile and multiply very quickly. Zookeeper now has $k$ rabbits and does not have enough carrots to feed all of them. To solve this problem, Zookeeper decided to cut the carrots into $k$ pieces. For some reason, all resulting carrot lengths must be positive integers.

Big carrots are very difficult for rabbits to handle and eat, so the time needed to eat a carrot of size $x$ is $x^2$.

Help Zookeeper split his carrots while minimizing the sum of time taken for rabbits to eat the carrots.


-----Input-----

The first line contains two integers $n$ and $k$ $(1 \leq n \leq k \leq 10^5)$: the initial number of carrots and the number of rabbits.

The next line contains $n$ integers $a_1, a_2, \ldots, a_n$ $(1 \leq a_i \leq 10^6)$: lengths of carrots.

It is guaranteed that the sum of $a_i$ is at least $k$.


-----Output-----

Output one integer: the minimum sum of time taken for rabbits to eat carrots.


-----Examples-----
Input
3 6
5 3 1

Output
15

Input
1 4
19

Output
91



-----Note-----

For the first test, the optimal sizes of carrots are $\{1,1,1,2,2,2\}$. The time taken is $1^2+1^2+1^2+2^2+2^2+2^2=15$

For the second test, the optimal sizes of carrots are $\{4,5,5,5\}$. The time taken is $4^2+5^2+5^2+5^2=91$.
"""

import heapq

def minimize_eating_time(n, k, carrot_lengths):
    def calc(l, n):
        smol = l // n
        tol = l % n
        return smol * smol * n + (2 * smol + 1) * tol
    
    curr = [1] * n
    q = []
    
    for i in range(n):
        v = carrot_lengths[i]
        heapq.heappush(q, (calc(v, 2) - calc(v, 1), i))
    
    out2 = sum([x * x for x in carrot_lengths])
    
    for i in range(k - n):
        (diff, nex) = heapq.heappop(q)
        curr[nex] += 1
        v = carrot_lengths[nex]
        heapq.heappush(q, (calc(v, curr[nex] + 1) - calc(v, curr[nex]), nex))
        out2 += diff
    
    out = 0
    for i in range(n):
        out += calc(carrot_lengths[i], curr[i])
    
    assert out == out2
    return out
"""
QUESTION:
Captain Fint is involved in another treasure hunt, but have found only one strange problem. The problem may be connected to the treasure's location or may not. That's why captain Flint decided to leave the solving the problem to his crew and offered an absurdly high reward: one day off. The problem itself sounds like this...

There are two arrays $a$ and $b$ of length $n$. Initially, an $ans$ is equal to $0$ and the following operation is defined:   Choose position $i$ ($1 \le i \le n$);  Add $a_i$ to $ans$;  If $b_i \neq -1$ then add $a_i$ to $a_{b_i}$. 

What is the maximum $ans$ you can get by performing the operation on each $i$ ($1 \le i \le n$) exactly once?

Uncle Bogdan is eager to get the reward, so he is asking your help to find the optimal order of positions to perform the operation on them.


-----Input-----

The first line contains the integer $n$ ($1 \le n \le 2 \cdot 10^5$) — the length of arrays $a$ and $b$.

The second line contains $n$ integers $a_1, a_2, \ldots, a_n$ ($−10^6 \le a_i \le 10^6$).

The third line contains $n$ integers $b_1, b_2, \ldots, b_n$ ($1 \le b_i \le n$ or $b_i = -1$).

Additional constraint: it's guaranteed that for any $i$ ($1 \le i \le n$) the sequence $b_i, b_{b_i}, b_{b_{b_i}}, \ldots$ is not cyclic, in other words it will always end with $-1$.


-----Output-----

In the first line, print the maximum $ans$ you can get.

In the second line, print the order of operations: $n$ different integers $p_1, p_2, \ldots, p_n$ ($1 \le p_i \le n$). The $p_i$ is the position which should be chosen at the $i$-th step. If there are multiple orders, print any of them.


-----Examples-----
Input
3
1 2 3
2 3 -1

Output
10
1 2 3 

Input
2
-1 100
2 -1

Output
99
2 1 

Input
10
-10 -1 2 2 5 -2 -3 -4 2 -6
-1 -1 2 2 -1 5 5 7 7 9

Output
-9
3 5 6 1 9 4 10 7 8 2
"""

def calculate_max_ans(n, a, b):
    adj = [0] * (n + 1)
    ind = [0] * (n + 1)
    
    for i in range(n):
        if b[i] != -1:
            adj[i + 1] = b[i]
            ind[b[i]] += 1
    
    q = deque()
    for i in range(1, n + 1):
        if not ind[i]:
            q.append(i)
    
    l = []
    ans = 0
    
    while q:
        cur = q.popleft()
        l.append(cur)
        ind[adj[cur]] -= 1
        if not ind[adj[cur]]:
            q.append(adj[cur])
    
    l1 = []
    l2 = deque()
    
    for i in l:
        if a[i - 1] >= 0:
            ans += a[i - 1]
            if b[i - 1] != -1:
                a[b[i - 1] - 1] += a[i - 1]
            l1.append(i)
        else:
            ans += a[i - 1]
            l2.appendleft(i)
    
    l2 = list(l2)
    l1 += l2
    
    return ans, l1
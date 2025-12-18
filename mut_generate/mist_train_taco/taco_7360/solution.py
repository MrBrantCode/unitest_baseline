"""
QUESTION:
You are given a complete directed graph $K_n$ with $n$ vertices: each pair of vertices $u \neq v$ in $K_n$ have both directed edges $(u, v)$ and $(v, u)$; there are no self-loops.

You should find such a cycle in $K_n$ that visits every directed edge exactly once (allowing for revisiting vertices).

We can write such cycle as a list of $n(n - 1) + 1$ vertices $v_1, v_2, v_3, \dots, v_{n(n - 1) - 1}, v_{n(n - 1)}, v_{n(n - 1) + 1} = v_1$ — a visiting order, where each $(v_i, v_{i + 1})$ occurs exactly once.

Find the lexicographically smallest such cycle. It's not hard to prove that the cycle always exists.

Since the answer can be too large print its $[l, r]$ segment, in other words, $v_l, v_{l + 1}, \dots, v_r$.


-----Input-----

The first line contains the single integer $T$ ($1 \le T \le 100$) — the number of test cases.

Next $T$ lines contain test cases — one per line. The first and only line of each test case contains three integers $n$, $l$ and $r$ ($2 \le n \le 10^5$, $1 \le l \le r \le n(n - 1) + 1$, $r - l + 1 \le 10^5$) — the number of vertices in $K_n$, and segment of the cycle to print.

It's guaranteed that the total sum of $n$ doesn't exceed $10^5$ and the total sum of $r - l + 1$ doesn't exceed $10^5$.


-----Output-----

For each test case print the segment $v_l, v_{l + 1}, \dots, v_r$ of the lexicographically smallest cycle that visits every edge exactly once.


-----Example-----
Input
3
2 1 3
3 3 6
99995 9998900031 9998900031

Output
1 2 1 
1 3 2 3 
1 



-----Note-----

In the second test case, the lexicographically minimum cycle looks like: $1, 2, 1, 3, 2, 3, 1$.

In the third test case, it's quite obvious that the cycle should start and end in vertex $1$.
"""

def find_lexicographically_smallest_cycle_segment(n, l, r):
    maximal = n * (n - 1) + 1
    
    if l == maximal:
        return [1]
    
    if r == maximal:
        end_1 = True
    else:
        end_1 = False
    
    result = []
    summa = 0
    i = (n - 1) * 2
    cnt = 0
    
    while summa + i < l:
        summa += i
        i -= 2
        cnt += 1
    
    l -= summa
    r -= summa
    summa = 0
    
    while l <= r:
        while l <= summa + i and l <= r:
            if l % 2 == 1:
                result.append(cnt + 1)
            else:
                result.append(cnt + l // 2 + 1)
            l += 1
        
        l -= i
        r -= i
        summa = 0
        i -= 2
        cnt += 1
        
        if i == 0 and end_1:
            result.append(1)
            break
    
    return result
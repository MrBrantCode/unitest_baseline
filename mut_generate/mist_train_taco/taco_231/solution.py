"""
QUESTION:
Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

You are given $N$ sets of integers $A_{1}, A_{2}, \ldots, A_{N}$. For each valid $i$, let's denote the elements of the set $A_{i}$ by $\{c_{i,1}, c_{i,2}, \ldots, c_{i,|A_{i}|}\}$.

Find the number of ways to choose a sequence $(a_{1}, a_{2}, \ldots, a_{N})$ such that:
$a_{i} \in A_{i}$ for each valid $i$
$a_{i} \neq a_{i+1}$ for each valid $i$ and $a_{1} \neq a_{N}$

Since this number may be large, compute it modulo $998,244,353$.

------  Input ------
The first line of the input contains a single integer $N$.
$N$ lines follow. For each valid $i$, the $i$-th of these lines contains an integer $|A_{i}|$ followed by a space and $|A_{i}|$ space-separated non-negative integers $c_{i,1}, c_{i,2}, \ldots, c_{i,|A_{i}|}$.

------  Output ------
Print a single line containing one integer ― the number of ways to choose $(a_{1}, a_{2}, \ldots, a_{N})$, modulo $998,244,353$.

------  Constraints  ------
$2 ≤ N ≤ 200,000$
$|A_{i}| ≥ 1$ for each valid $i$
$|A_{1}| + |A_{2}| + \ldots + |A_{N}| ≤ 200,000$
$1 ≤ c_{i,j} ≤ 200000$ for each valid $i, j$

------  Subtasks ------
Subtask #1 (20 points): $N ≤ 100$

Subtask #2 (80 points): original constraints

----- Sample Input 1 ------ 
3

3 1 2 3

2 1 2

2 2 3
----- Sample Output 1 ------ 
3
----- explanation 1 ------ 
There are three possible sequences: $(1, 2, 3)$, $(2, 1, 3)$ and $(3, 1, 2)$.
"""

MOD = 998244353

def count_valid_sequences(N, sets):
    def calc(arr):
        vars = {i: 1 for i in arr[0]}
        for i in range(1, len(arr)):
            tot = sum(vars.values()) % MOD
            next = {}
            for num in arr[i]:
                cur = tot
                if num in vars:
                    cur += MOD - vars[num]
                cur %= MOD
                next[num] = cur
            vars = next
        return sum(vars.values()) % MOD

    if N <= 450:
        ans = 0
        sign = False
        while len(sets) > 1:
            cur = calc(sets)
            if sign:
                cur = MOD - cur
            ans += cur
            ans %= MOD
            sets[0] = list(set(sets[0]).intersection(set(sets[-1])))
            sets[0].sort()
            del sets[-1:]
            sign = not sign
        return ans
    else:
        best = 10 ** 15
        mem = -1
        saved_set = []
        for i in range(N):
            prev = (i + N - 1) % N
            t = set(sets[i]).intersection(set(sets[prev]))
            sz = len(t)
            if sz < best:
                best = sz
                mem = i
                saved_set = list(t)
        sets = sets[mem:] + sets[:mem]
        ans = calc(sets)
        saved_set.sort()
        for val in saved_set:
            sets[0] = [val]
            sets[-1] = [val]
            ans += MOD - calc(sets)
            ans %= MOD
        return ans
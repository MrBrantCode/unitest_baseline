"""
QUESTION:
$n$ people gathered to hold a jury meeting of the upcoming competition, the $i$-th member of the jury came up with $a_i$ tasks, which they want to share with each other.

First, the jury decides on the order which they will follow while describing the tasks. Let that be a permutation $p$ of numbers from $1$ to $n$ (an array of size $n$ where each integer from $1$ to $n$ occurs exactly once).

Then the discussion goes as follows:

If a jury member $p_1$ has some tasks left to tell, then they tell one task to others. Otherwise, they are skipped.

If a jury member $p_2$ has some tasks left to tell, then they tell one task to others. Otherwise, they are skipped.

...

If a jury member $p_n$ has some tasks left to tell, then they tell one task to others. Otherwise, they are skipped.

If there are still members with tasks left, then the process repeats from the start. Otherwise, the discussion ends.

A permutation $p$ is nice if none of the jury members tell two or more of their own tasks in a row.

Count the number of nice permutations. The answer may be really large, so print it modulo $998\,244\,353$.


-----Input-----

The first line contains a single integer $t$ ($1 \le t \le 10^4$) — the number of test cases.

The first line of the test case contains a single integer $n$ ($2 \le n \le 2 \cdot 10^5$) — number of jury members.

The second line contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 10^9$) — the number of problems that the $i$-th member of the jury came up with.

The sum of $n$ over all test cases does not exceed $2 \cdot 10^5$.


-----Output-----

For each test case, print one integer — the number of nice permutations, taken modulo $998\,244\,353$.


-----Examples-----

Input
4
2
1 2
3
5 5 5
4
1 3 3 7
6
3 4 2 1 3 3
Output
1
6
0
540


-----Note-----

Explanation of the first test case from the example:

There are two possible permutations, $p = [1, 2]$ and $p = [2, 1]$. For $p = [1, 2]$, the process is the following:

the first jury member tells a task;

the second jury member tells a task;

the first jury member doesn't have any tasks left to tell, so they are skipped;

the second jury member tells a task.

So, the second jury member has told two tasks in a row (in succession), so the permutation is not nice.

For $p = [2, 1]$, the process is the following:

the second jury member tells a task;

the first jury member tells a task;

the second jury member tells a task.

So, this permutation is nice.
"""

def count_nice_permutations(n, tasks):
    mod = 998244353
    mx = 2 * 10 ** 5 + 2
    fact = [0] * (mx + 1)
    inv_fact = [0] * (mx + 1)
    
    # Precompute factorials and inverse factorials
    fact[0] = 1
    for i in range(mx):
        fact[i + 1] = fact[i] * (i + 1) % mod
    inv_fact[-1] = pow(fact[-1], mod - 2, mod)
    for i in reversed(range(mx)):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    
    # Sort the tasks list
    sorted_tasks = sorted(tasks)
    
    # Check the conditions for nice permutations
    if sorted_tasks[-1] - sorted_tasks[-2] > 1:
        return 0
    elif sorted_tasks[-1] == sorted_tasks[-2]:
        return fact[n]
    else:
        k = sorted_tasks.count(sorted_tasks[-2])
        return (fact[n] - fact[n] * fact[k] * inv_fact[k + 1]) % mod
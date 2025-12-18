"""
QUESTION:
You are given an array $a$ of length $n$. Let $cnt_x$ be the number of elements from the array which are equal to $x$. Let's also define $f(x, y)$ as $(cnt_x + cnt_y) \cdot (x + y)$.

Also you are given $m$ bad pairs $(x_i, y_i)$. Note that if $(x, y)$ is a bad pair, then $(y, x)$ is also bad.

Your task is to find the maximum value of $f(u, v)$ over all pairs $(u, v)$, such that $u \neq v$, that this pair is not bad, and also that $u$ and $v$ each occur in the array $a$. It is guaranteed that such a pair exists.


-----Input-----

The first line contains a single integer $t$ ($1 \le t \le 10000$) — the number of test cases.

The first line of each test case contains two integers $n$ and $m$ ($2 \le n \le 3 \cdot 10^5$, $0 \le m \le 3 \cdot 10^5$) — the length of the array and the number of bad pairs.

The second line of each test case contains $n$ integers $a_1, a_2, \ldots, a_n$ ($1 \le a_i \le 10^9$) — elements of the array.

The $i$-th of the next $m$ lines contains two integers $x_i$ and $y_i$ ($1 \le x_i < y_i \le 10^9$), which represent a bad pair. It is guaranteed that no bad pair occurs twice in the input. It is also guaranteed that $cnt_{x_i} > 0$ and $cnt_{y_i} > 0$.

It is guaranteed that for each test case there is a pair of integers $(u, v)$, $u \ne v$, that is not bad, and such that both of these numbers occur in $a$.

It is guaranteed that the total sum of $n$ and the total sum of $m$ don't exceed $3 \cdot 10^5$.


-----Output-----

For each test case print a single integer — the answer to the problem.


-----Examples-----

Input
3
6 1
6 3 6 7 3 3
3 6
2 0
3 4
7 4
1 2 2 3 1 5 1
1 5
3 5
1 3
2 5
Output
40
14
15


-----Note-----

In the first test case $3$, $6$, $7$ occur in the array.

$f(3, 6) = (cnt_3 + cnt_6) \cdot (3 + 6) = (3 + 2) \cdot (3 + 6) = 45$. But $(3, 6)$ is bad so we ignore it.

$f(3, 7) = (cnt_3 + cnt_7) \cdot (3 + 7) = (3 + 1) \cdot (3 + 7) = 40$.

$f(6, 7) = (cnt_6 + cnt_7) \cdot (6 + 7) = (2 + 1) \cdot (6 + 7) = 39$.

The answer to the problem is $\max(40, 39) = 40$.
"""

def find_max_f_value(n, m, a, bad_pairs):
    from collections import defaultdict
    
    # Count occurrences of each element in the array
    cnt = defaultdict(int)
    for num in a:
        cnt[num] += 1
    
    # Convert bad pairs to a set for O(1) lookup
    bad = set(bad_pairs)
    
    # Sort the array in descending order
    a.sort(reverse=True)
    
    # Group elements by their counts
    count_groups = defaultdict(list)
    for num in a:
        count_groups[cnt[num]].append(num)
    
    best = -1
    
    # Iterate over count groups to find the maximum f(u, v)
    for count_u, group_u in count_groups.items():
        for count_v, group_v in count_groups.items():
            if count_u < count_v:
                continue
            for u in group_u:
                for v in group_v:
                    if u != v:
                        if (u, v) not in bad and (v, u) not in bad:
                            best = max(best, (cnt[u] + cnt[v]) * (u + v))
                            break
    
    return best
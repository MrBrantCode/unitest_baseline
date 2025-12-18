"""
QUESTION:
Given an array $a_1, a_2, \dots, a_n$, you need to handle a total of $q$ updates and queries of two types:

$1$ $l$ $r$ — for each index $i$ with $l \leq i \leq r$, update the value of $a_i$ to the sum of the digits of $a_i$.

$2$ $x$ — output $a_x$.


-----Input-----

The first line of the input contains an integer $t$ ($1 \leq t \leq 1000$) — the number of testcases.

The first line of each test case contains two integers $n$ and $q$ ($1 \le n, q \le 2 \cdot 10^5$) — the size of the array and the number of queries, respectively.

The second line of each test case contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 10^9$).

The next $q$ lines of each test case are of two forms:

$1$ $l$ $r$ ($1 \leq l \leq r \leq n$) — it means, for each index $i$ with $l \leq i \leq r$, you should update the value of $a_i$ to the sum of its digits.

$2$ $x$ ($1 \leq x \leq n$) — it means you should output $a_x$.

There is at least one query of the second type.

The sum of $n$ over all test cases does not exceed $2 \cdot 10^5$.

The sum of $q$ over all test cases does not exceed $2 \cdot 10^5$.


-----Output-----

For each test case, output the answers of queries of the second type, in the order they are given.


-----Examples-----

Input
3
5 8
1 420 69 1434 2023
1 2 3
2 2
2 3
2 4
1 2 5
2 1
2 3
2 5
2 3
9999 1000
1 1 2
2 1
2 2
1 1
1
2 1
Output
6
15
1434
1
6
7
36
1
1


-----Note-----

In the first test case, the following process occurs:

Initially, $a = [1, 420, 69, 1434, 2023]$.

The operation is performed for $l=2$, $r=3$, yielding $[1, {6}, {15}, 1434, 2023]$.

We are queried for $x=2$, $x=3$, and $x=4$, and output $6$, $15$, and $1434$.

The operation is performed for $l=2$, $r=5$, yielding $[1, {6}, {6}, {12}, {7}]$.

We are queried for $x=1$, $x=3$, and $x=5$, and output $1$, $6$, and $7$.
"""

def process_queries(n, test_cases):
    def find(x, fa):
        t = x
        while fa[x] != x:
            x = fa[x]
        while t != x:
            (fa[t], t) = (x, fa[t])
        return x

    def union(son, father, fa):
        x = find(son, fa)
        y = find(father, fa)
        fa[x] = y

    def f(num):
        ans = 0
        while num > 0:
            ans += num % 10
            num //= 10
        return ans

    results = []

    for test_case in test_cases:
        m, q, array, queries = test_case
        fa = list(range(m + 1))
        output_results = []

        for query in queries:
            if query[0] == 1:
                l, r = query[1], query[2]
                l -= 1
                l = find(l, fa)
                while l < r:
                    array[l] = f(array[l])
                    if array[l] < 10:
                        union(l, l + 1, fa)
                    l = find(l + 1, fa)
            elif query[0] == 2:
                x = query[1] - 1
                output_results.append(array[x])

        results.append(output_results)

    return results
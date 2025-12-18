"""
QUESTION:
You are given an array $a$ of $n$ non-negative integers. In one operation you can change any number in the array to any other non-negative integer.

Let's define the cost of the array as $\operatorname{DIFF}(a) - \operatorname{MEX}(a)$, where $\operatorname{MEX}$ of a set of non-negative integers is the smallest non-negative integer not present in the set, and $\operatorname{DIFF}$ is the number of different numbers in the array.

For example, $\operatorname{MEX}(\{1, 2, 3\}) = 0$, $\operatorname{MEX}(\{0, 1, 2, 4, 5\}) = 3$.

You should find the minimal cost of the array $a$ if you are allowed to make at most $k$ operations.


-----Input-----

The input consists of multiple test cases. The first line contains a single integer $t$ ($1 \le t \le 10^4$) — the number of test cases. Description of the test cases follows.

The first line of each test case contains two integers $n$ and $k$ ($1 \le n \le 10^5$, $0 \le k \le 10^5$) — the length of the array $a$ and the number of operations that you are allowed to make.

The second line of each test case contains $n$ integers $a_1, a_2, \ldots, a_n$ ($0 \le a_i \le 10^9$) — the elements of the array $a$.

It is guaranteed that the sum of $n$ over all test cases does not exceed $10^5$.


-----Output-----

For each test case output a single integer — minimal cost that it is possible to get making at most $k$ operations.


-----Examples-----

Input
4
4 1
3 0 1 2
4 1
0 2 4 5
7 2
4 13 0 0 13 1337 1000000000
6 2
1 2 8 0 0 0
Output
0
1
2
0


-----Note-----

In the first test case no operations are needed to minimize the value of $\operatorname{DIFF} - \operatorname{MEX}$.

In the second test case it is possible to replace $5$ by $1$. After that the array $a$ is $[0,\, 2,\, 4,\, 1]$, $\operatorname{DIFF} = 4$, $\operatorname{MEX} = \operatorname{MEX}(\{0, 1, 2, 4\}) = 3$, so the answer is $1$.

In the third test case one possible array $a$ is $[4,\, 13,\, 0,\, 0,\, 13,\, 1,\, 2]$, $\operatorname{DIFF} = 5$, $\operatorname{MEX} = 3$.

In the fourth test case one possible array $a$ is $[1,\, 2,\, 3,\, 0,\, 0,\, 0]$.
"""

import heapq
from collections import Counter

def calculate_minimal_cost(arr, k):
    # Sort the array to facilitate finding MEX
    arr.sort()
    
    # Count the frequency of each number in the array
    cnt = Counter(arr)
    
    # Find the MEX (Minimum Excludant)
    mex = 0
    for i in range(len(arr) + 1):
        if i not in cnt:
            if k > 0:
                k -= 1
            else:
                mex = i
                break
    
    # If mex is still 0, it means we can reach the end of the array without running out of operations
    if mex == 0:
        return 0
    
    # Collect counts of numbers greater than or equal to MEX
    v = []
    for key in cnt:
        if key >= mex:
            heapq.heappush(v, cnt[key])
    
    # Calculate the initial cost
    cost = len(v)
    
    # Reduce the cost by using the allowed operations
    while v:
        if v[0] <= k:
            k -= v[0]
            heapq.heappop(v)
            cost -= 1
        else:
            break
    
    return cost
"""
QUESTION:
You are given an array A of N positive integers. 

In one operation, you can do the following:
Choose an index i (1 ≤ i ≤ N), and change the value of A_{i} to either (A_{i})^2 or \lfloor \sqrt{A_{i}} \rfloor.

Find the minimum number of operations required, such that, for the final array A:
A is sorted in non-decreasing order;
A_{N} ≤ 10^{18}.

NOTE: The elements of the array might not fit in a 32-bit integer.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of two lines of input:
- The first line of each test case contains N - the size of the array.
- The next line contains N integers, A_{1}, A_{2}, A_{3}, \ldots, A_{N} - the elements of the array.

------ Output Format ------ 

For each test case, output on a new line, the minimum number of operations required.

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$1 ≤ N ≤ 10^{5}$
$1 ≤ A_{i} ≤ 10^{18}$
- The sum of $N$ over all test cases won't exceed $10^{5}$.

----- Sample Input 1 ------ 
3
4
1 3 9 9
4
1 9 3 9
3
4 2 1

----- Sample Output 1 ------ 
0
1
3

----- explanation 1 ------ 
Test case $1$: The array is already sorted, no operation is required.

Test case $2$: Using one operation, we can change $A_{2}$ to $\lfloor \sqrt{A_{2}}\rfloor = 3$. The final array is $A = [1, 3, 3, 9]$ which is sorted in non-decreasing order.

Test case $3$: We make the following operations:
- Change $A_{2}$ to $\lfloor \sqrt{A_{2}}\rfloor = 1$.
- Change $A_{1}$ to $\lfloor \sqrt{A_{1}}\rfloor = 2$.
- Change $A_{1}$ to $\lfloor \sqrt{A_{1}}\rfloor = 1$.

The final array is $A = [1, 1, 1]$ which is sorted in non-decreasing order.
"""

from collections import deque
import math

def getsqrt(x):
    s = int(math.sqrt(x))
    while (s + 1) * (s + 1) <= x:
        s += 1
    while s * s > x:
        s -= 1
    return s

def bfs(x):
    queue = [[x, 0]]
    reached = set([x])
    for (u, d) in queue:
        if u <= 10 ** 9 and u * u not in reached:
            reached.add(u * u)
            queue.append([u * u, d + 1])
        y = getsqrt(u)
        if y not in reached:
            reached.add(y)
            queue.append([y, d + 1])
    return sorted(queue)

def min_operations_to_sort_array(test_cases):
    results = []
    for n, a in test_cases:
        prv = [[1, 0]]
        for x in a:
            costs = bfs(x)
            dp = []
            (ptr, mn) = (0, 10 ** 18)
            for (y, d) in costs:
                while ptr < len(prv) and prv[ptr][0] <= y:
                    mn = min(mn, prv[ptr][1])
                    ptr += 1
                dp.append([y, d + mn])
            prv = dp
        ans = 10 ** 18
        for (x, d) in prv:
            ans = min(ans, d)
        results.append(ans)
    return results
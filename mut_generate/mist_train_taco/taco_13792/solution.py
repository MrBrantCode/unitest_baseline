"""
QUESTION:
Read problem statements in [Mandarin], [Vietnamese], and [Russian] as well.

You are given a positive integer K and an array A consisting of N non-negative integers. Find the [lexicographically] smallest sequence B that satisfies the following conditions

We can obtain B by rearranging the elements in A.
The length of longest non-decreasing [subsequence] of B is equal to K.

If no such sequence exists, print -1.

------ Input Format ------ 

- First line of the input contains T, the number of testcases. Then the testcases follow.
- First line of each test case contains two space separated integers N and K.
- Second line of each test case contains N space separated integers describing the array A.

------ Output Format ------ 

For each test case, output the array B in a single line with a space between two consecutive elements. And output -1 if no such array B exists.

------ Constraints ------ 

$1 ≤ T ≤ 200$
$1 ≤ N ≤ 200$
$1 ≤ K ≤ N$
$1 ≤ A_{i} ≤ N$
- Sum of $N$ over all test cases doesn't exceed $200$.

----- Sample Input 1 ------ 
4
3 1
2 1 3
3 2
2 1 3
3 3
2 1 3
3 1
2 2 3

----- Sample Output 1 ------ 
3 2 1
1 3 2
1 2 3
-1

----- explanation 1 ------ 
There are $6$ arrays that are rearrangements of the array $[2, 1, 3]$.

- $[1, 2, 3]$ with length of longest non-decreasing subsequence equal to $3$.
- $[1, 3, 2]$ with length of longest non-decreasing subsequence equal to $2$.
- $[2, 1, 3]$ with length of longest non-decreasing subsequence equal to $2$.
- $[2, 3, 1]$ with length of longest non-decreasing subsequence equal to $2$.
- $[3, 1, 2]$ with length of longest non-decreasing subsequence equal to $2$.
- $[3, 2, 1]$ with length of longest non-decreasing subsequence equal to $1$.

Test case 1:

Observe from the list above that $[3, 2, 1]$ is the only rearrangement of $[2, 1, 3]$ with the length of the longest non-decreasing subsequence equal to $1$. And hence $[3, 2, 1]$ is the lexicographically smallest that satisfies the given conditions.

Test case 2:

Observe from the above list the $[1, 3, 2]$ is the lexicographically smallest among all those rearrangements with the length of the longest non-decreasing subsequence equal to $2$. And hence $[1, 3, 2]$ is the lexicographically smallest that satisfies the given conditions.

Test case 3:

Observe from the list above that $[1, 2, 3]$ is the only rearrangement of $[2, 1, 3]$ with the length of the longest non-decreasing subsequence equal to $3$. And hence $[1, 2, 3]$ is the lexicographically smallest that satisfies the given conditions.

Test case 4:

There are only $3$ possible ways to rearrange $[2, 2, 3]$.

- $[2, 2, 3]$ with length of longest non-decreasing subsequence equal to $3$.
- $[2, 3, 2]$ with length of longest non-decreasing subsequence equal to $2$.
- $[3, 2, 2]$ with length of longest non-decreasing subsequence equal to $2$.

So there does not exist any rearrangement of $[2, 2, 3]$ with the length of the longest non-decreasing subsequence equal to $1$.
"""

from bisect import bisect_right

def find_lexicographically_smallest_sequence(N, K, A):
    def lis(a):
        n = len(a)
        INF = float('inf')
        d = [INF] * (n + 1)
        d[0] = -INF
        for i in range(n):
            j = bisect_right(d, a[i])
            if d[j - 1] <= a[i] < d[j]:
                d[j] = a[i]
        ans = 0
        for i in range(n + 1):
            if d[i] < INF:
                ans = i
        return ans
    
    a = sorted(A)
    c = a[:K]
    for i in range(K, N):
        for j in reversed(range(len(c))):
            b = c[:j] + [a[i]] + c[j:]
            if lis(b) == K:
                c = b
                break
    
    if lis(c) != K or sorted(c) != a:
        return -1
    else:
        return c
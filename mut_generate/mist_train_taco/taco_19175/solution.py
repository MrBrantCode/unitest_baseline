"""
QUESTION:
Read problem statements in [Mandarin], [Bengali], [Russian], and [Vietnamese] as well.

Chef has a sequence A_{1}, A_{2}, \ldots, A_{N}. Let's call a contiguous subsequence of A a *segment*.

A segment is *good* if it can be divided into at most K segments such that the sum of elements in each of these sub-segments is at most S.

You need to find the maximum number of elements in a good segment.

------ Input Format ------ 

- The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
- The first line of each test case contains three space-separated integers N, K and S.
- The second line contains N space-separated integers A_{1}, A_{2}, \ldots, A_{N}.

------ Output Format ------ 

For each test case, print a single line containing one integer — the maximum length of a good segment.

------ Constraints ------ 

$1 ≤T ≤150,000$
$1 ≤K ≤N ≤10^{5}$
$1 ≤S ≤10^{9}$
$1 ≤A_{i} ≤S$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $10^{6}$

------ subtasks ------ 

Subtask #1 (100 points): original constraints

----- Sample Input 1 ------ 
2
5 2 5
1 3 2 1 5
5 3 5
5 1 5 1 1
----- Sample Output 1 ------ 
4
4
----- explanation 1 ------ 
Example case 1: One of the segments with length $4$ is $[1, 3, 2, 1]$. It can be divided into two segments $[1, 3]$ and $[2, 1]$ whose sums are at most $S = 5$.
"""

def find_max_good_segment_length(nums, N, K, S):
    def build(N, start_index):
        up = [[None] * N for _ in range(20)]
        up[0] = start_index
        for i in range(1, 20):
            for j in range(N):
                p = up[i - 1][j]
                if p == -1:
                    up[i][j] = -1
                else:
                    up[i][j] = up[i - 1][p]
        return up

    def call(up, node, K):
        (last, jump) = (node, 1)
        for i in range(19):
            if node == -1:
                break
            if K & jump:
                node = up[i][node]
            jump <<= 1
        return last - node

    (start_index, j, curr) = ([], 0, 0)
    for i in range(N):
        curr += nums[i]
        while curr > S:
            curr -= nums[j]
            j += 1
        start_index.append(j - 1)
    up = build(N, start_index)
    res = 0
    for i in range(N - 1, -1, -1):
        res = max(res, call(up, i, K))
    return res
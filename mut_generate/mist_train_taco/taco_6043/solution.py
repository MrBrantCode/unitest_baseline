"""
QUESTION:
Recently Lynyrd and Skynyrd went to a shop where Lynyrd bought a permutation p of length n, and Skynyrd bought an array a of length m, consisting of integers from 1 to n. 

Lynyrd and Skynyrd became bored, so they asked you q queries, each of which has the following form: "does the subsegment of a from the l-th to the r-th positions, inclusive, have a subsequence that is a cyclic shift of p?" Please answer the queries.

A permutation of length n is a sequence of n integers such that each integer from 1 to n appears exactly once in it.

A cyclic shift of a permutation (p_1, p_2, …, p_n) is a permutation (p_i, p_{i + 1}, …, p_{n}, p_1, p_2, …, p_{i - 1}) for some i from 1 to n. For example, a permutation (2, 1, 3) has three distinct cyclic shifts: (2, 1, 3), (1, 3, 2), (3, 2, 1).

A subsequence of a subsegment of array a from the l-th to the r-th positions, inclusive, is a sequence a_{i_1}, a_{i_2}, …, a_{i_k} for some i_1, i_2, …, i_k such that l ≤ i_1 < i_2 < … < i_k ≤ r.

Input

The first line contains three integers n, m, q (1 ≤ n, m, q ≤ 2 ⋅ 10^5) — the length of the permutation p, the length of the array a and the number of queries.

The next line contains n integers from 1 to n, where the i-th of them is the i-th element of the permutation. Each integer from 1 to n appears exactly once.

The next line contains m integers from 1 to n, the i-th of them is the i-th element of the array a.

The next q lines describe queries. The i-th of these lines contains two integers l_i and r_i (1 ≤ l_i ≤ r_i ≤ m), meaning that the i-th query is about the subsegment of the array from the l_i-th to the r_i-th positions, inclusive.

Output

Print a single string of length q, consisting of 0 and 1, the digit on the i-th positions should be 1, if the subsegment of array a from the l_i-th to the r_i-th positions, inclusive, contains a subsequence that is a cyclic shift of p, and 0 otherwise.

Examples

Input

3 6 3
2 1 3
1 2 3 1 2 3
1 5
2 6
3 5


Output

110


Input

2 4 3
2 1
1 1 2 2
1 2
2 3
3 4


Output

010

Note

In the first example the segment from the 1-st to the 5-th positions is 1, 2, 3, 1, 2. There is a subsequence 1, 3, 2 that is a cyclic shift of the permutation. The subsegment from the 2-nd to the 6-th positions also contains a subsequence 2, 1, 3 that is equal to the permutation. The subsegment from the 3-rd to the 5-th positions is 3, 1, 2, there is only one subsequence of length 3 (3, 1, 2), but it is not a cyclic shift of the permutation.

In the second example the possible cyclic shifts are 1, 2 and 2, 1. The subsegment from the 1-st to the 2-nd positions is 1, 1, its subsequences are not cyclic shifts of the permutation. The subsegment from the 2-nd to the 3-rd positions is 1, 2, it coincides with the permutation. The subsegment from the 3 to the 4 positions is 2, 2, its subsequences are not cyclic shifts of the permutation.
"""

def has_cyclic_shift_subsequence(n, m, q, p, a, queries):
    from math import log, floor
    
    logit = floor(log(n) // log(2)) + 1
    current_max_index = [-1] * (n + 1)
    prevs = [[-1] * m for i in range(logit)]
    prev_map = [-2] * (n + 1)
    
    for (i, j) in zip(p[1:] + [p[0]], p):
        prev_map[i] = j
    
    for (idx, ele) in enumerate(a):
        prevs[0][idx] = current_max_index[prev_map[ele]]
        current_max_index[ele] = idx
    
    for i in range(1, logit):
        for (idx, ele) in enumerate(a):
            if prevs[i - 1][idx] != -1:
                prevs[i][idx] = prevs[i - 1][prevs[i - 1][idx]]
    
    use = [i for i in range(n.bit_length()) if 1 & (n - 1) >> i]
    max_pre = -1
    ran = [-1] * (m + 2)
    
    for i in range(m):
        t = i
        for dim in use:
            t = prevs[dim][t]
            if t == -1:
                break
        max_pre = max(t, max_pre)
        ran[i] = max_pre
    
    ans = [None] * q
    for i in range(q):
        (l, r) = queries[i]
        ans[i] = str(int(l - 1 <= ran[r - 1]))
    
    return ans
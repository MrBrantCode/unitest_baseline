"""
QUESTION:
For the given sequence with n different elements find the number of increasing subsequences with k + 1 elements. It is guaranteed that the answer is not greater than 8·1018.

Input

First line contain two integer values n and k (1 ≤ n ≤ 105, 0 ≤ k ≤ 10) — the length of sequence and the number of elements in increasing subsequences.

Next n lines contains one integer ai (1 ≤ ai ≤ n) each — elements of sequence. All values ai are different.

Output

Print one integer — the answer to the problem.

Examples

Input

5 2
1
2
3
5
4


Output

7
"""

def count_increasing_subsequences(n, k, sequence):
    si = 1 << (n.bit_length() - (not n & (n - 1)))
    dp = [[0] * n for _ in range(k + 1)]
    dp[0] = [1] * n
    
    def update(tree, pos, diff, si):
        pos += si - 1
        while pos:
            tree[pos] += diff
            pos >>= 1
    
    def query(tree, l, r, si):
        ans, l, r = 0, l + si - 1, r + si - 1
        while l < r:
            if l & 1:
                ans += tree[l]
                l += 1
            if not r & 1:
                ans += tree[r]
                r -= 1
            l, r = l >> 1, r >> 1
        return ans + (0 if l != r else tree[l])
    
    for i in range(1, k + 1):
        tree = [0] * (si << 1)
        for j in range(n):
            dp[i][j] = query(tree, 1, sequence[j], si)
            update(tree, sequence[j], dp[i - 1][j], si)
    
    return sum(dp[-1])
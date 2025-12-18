"""
QUESTION:
Gargari got bored to play with the bishops and now, after solving the problem about them, he is trying to do math homework. In a math book he have found k permutations. Each of them consists of numbers 1, 2, ..., n in some order. Now he should find the length of the longest common subsequence of these permutations. Can you help Gargari?

You can read about longest common subsequence there: https://en.wikipedia.org/wiki/Longest_common_subsequence_problem


-----Input-----

The first line contains two integers n and k (1 ≤ n ≤ 1000; 2 ≤ k ≤ 5). Each of the next k lines contains integers 1, 2, ..., n in some order — description of the current permutation.


-----Output-----

Print the length of the longest common subsequence.


-----Examples-----
Input
4 3
1 4 2 3
4 1 2 3
1 2 4 3

Output
3



-----Note-----

The answer for the first test sample is subsequence [1, 2, 3].
"""

def longest_common_subsequence_length(n, k, permutations):
    a = [list(map(lambda x: int(x) - 1, perm)) for perm in permutations]
    b = [[0] * n for _ in range(k)]
    for i in range(k):
        for j in range(n):
            b[i][a[i][j]] = j
    dp = [[0] * n for _ in range(k)]
    for i in range(n - 1, -1, -1):
        for j in range(k):
            (maa, ele) = (0, a[j][i])
            for m in range(k):
                if b[m][ele] < i:
                    break
            else:
                for l in range(b[j][ele] + 1, n):
                    ma = 0
                    for m in range(k):
                        if b[m][ele] > b[m][a[j][l]]:
                            break
                        ma = max(ma, dp[m][b[m][a[j][l]]])
                    else:
                        maa = max(maa, ma)
                dp[j][i] = maa + 1
    return max((max(i) for i in dp))
"""
QUESTION:
There are N panels arranged in a row in Takahashi's house, numbered 1 through N. The i-th panel has a number A_i written on it. Takahashi is playing by throwing balls at these panels.

Takahashi threw a ball K times. Let the panel hit by a boll in the i-th throw be panel p_i. He set the score for the i-th throw as i \times A_{p_i}.

He was about to calculate the total score for his throws, when he realized that he forgot the panels hit by balls, p_1,p_2,...,p_K. The only fact he remembers is that for every i (1 ≦ i ≦ K-1), 1 ≦ p_{i+1}-p_i ≦ M holds. Based on this fact, find the maximum possible total score for his throws.

Constraints

* 1 ≦ M ≦ N ≦ 100,000
* 1 ≦ K ≦ min(300,N)
* 1 ≦ A_i ≦ 10^{9}

Input

The input is given from Standard Input in the following format:


N M K
A_1 A_2 … A_N


Output

Print the maximum possible total score for Takahashi's throws.

Examples

Input

5 2 3
10 2 8 10 2


Output

56


Input

5 5 2
5 2 10 5 9


Output

28


Input

10 3 5
3 7 2 6 9 4 8 5 1 1000000000


Output

5000000078
"""

from collections import deque

def calculate_max_total_score(N, M, K, A):
    dp = [0] * (N + 1)
    for j in range(K):
        newDP = [0] * (N + 1)
        que = deque()
        for i in range(j, N - K + j + 1):
            while que and que[-1][0] < dp[i]:
                que.pop()
            que.append((dp[i], i))
            while que and que[0][1] <= i - M:
                que.popleft()
            newDP[i + 1] = que[0][0] + (j + 1) * A[i]
        dp = newDP
    return max(dp)
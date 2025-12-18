"""
QUESTION:
The finalists of the "Russian Code Cup" competition in 2214 will be the participants who win in one of the elimination rounds.

The elimination rounds are divided into main and additional. Each of the main elimination rounds consists of c problems, the winners of the round are the first n people in the rating list. Each of the additional elimination rounds consists of d problems. The winner of the additional round is one person. Besides, k winners of the past finals are invited to the finals without elimination.

As a result of all elimination rounds at least n·m people should go to the finals. You need to organize elimination rounds in such a way, that at least n·m people go to the finals, and the total amount of used problems in all rounds is as small as possible.


-----Input-----

The first line contains two integers c and d (1 ≤ c, d ≤ 100) — the number of problems in the main and additional rounds, correspondingly. The second line contains two integers n and m (1 ≤ n, m ≤ 100). Finally, the third line contains an integer k (1 ≤ k ≤ 100) — the number of the pre-chosen winners. 


-----Output-----

In the first line, print a single integer — the minimum number of problems the jury needs to prepare.


-----Examples-----
Input
1 10
7 2
1

Output
2

Input
2 2
2 1
2

Output
0
"""

def calculate_minimum_problems(c: int, d: int, n: int, m: int, k: int) -> int:
    dp = [0] * 100000
    need = n * m - k
    
    if need <= 0:
        return 0
    
    for i in range(1, 100000):
        dp[i] = min(dp[i - n] + c, dp[i - 1] + d)
    
    return dp[need]
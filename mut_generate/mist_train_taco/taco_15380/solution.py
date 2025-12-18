"""
QUESTION:
Vladik was bored on his way home and decided to play the following game. He took n cards and put them in a row in front of himself. Every card has a positive integer number not exceeding 8 written on it. He decided to find the longest subsequence of cards which satisfies the following conditions:

  the number of occurrences of each number from 1 to 8 in the subsequence doesn't differ by more then 1 from the number of occurrences of any other number. Formally, if there are c_{k} cards with number k on them in the subsequence, than for all pairs of integers $i \in [ 1,8 ], j \in [ 1,8 ]$ the condition |c_{i} - c_{j}| ≤ 1 must hold.  if there is at least one card with number x on it in the subsequence, then all cards with number x in this subsequence must form a continuous segment in it (but not necessarily a continuous segment in the original sequence). For example, the subsequence [1, 1, 2, 2] satisfies this condition while the subsequence [1, 2, 2, 1] doesn't. Note that [1, 1, 2, 2] doesn't satisfy the first condition. 

Please help Vladik to find the length of the longest subsequence that satisfies both conditions.


-----Input-----

The first line contains single integer n (1 ≤ n ≤ 1000) — the number of cards in Vladik's sequence.

The second line contains the sequence of n positive integers not exceeding 8 — the description of Vladik's sequence.


-----Output-----

Print single integer — the length of the longest subsequence of Vladik's sequence that satisfies both conditions.


-----Examples-----
Input
3
1 1 1

Output
1
Input
8
8 7 6 5 4 3 2 1

Output
8
Input
24
1 8 1 2 8 2 3 8 3 4 8 4 5 8 5 6 8 6 7 8 7 8 8 8

Output
17


-----Note-----

In the first sample all the numbers written on the cards are equal, so you can't take more than one card, otherwise you'll violate the first condition.
"""

import copy

def find_longest_valid_subsequence(n, cards):
    a = [card - 1 for card in cards]
    nextcard = [[-1 for _ in range(8)] for _ in range(n)]
    
    for i in range(n - 2, -1, -1):
        nextcard[i] = copy.copy(nextcard[i + 1])
        nextcard[i][a[i + 1]] = i + 1
    
    jump = [[-1 for _ in range(n + 1)] for _ in range(n)]
    for i in range(n):
        card = a[i]
        cpos = i
        j = 1
        while cpos != -1:
            jump[i][j] = cpos
            j += 1
            cpos = nextcard[cpos][card]

    def getLen(val):
        dp = [[-1 for _ in range(1 << 8)] for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(n):
            card = a[i]
            for comb in range(1 << 8):
                if comb & 1 << card == 0 and dp[i][comb] != -1:
                    ncomb = comb + (1 << card)
                    if jump[i][val] != -1:
                        j = jump[i][val] + 1
                        dp[j][ncomb] = max(dp[j][ncomb], dp[i][comb] + val)
                    if jump[i][val + 1] != -1:
                        j = jump[i][val + 1] + 1
                        dp[j][ncomb] = max(dp[j][ncomb], dp[i][comb] + val + 1)
                dp[i + 1][comb] = max(dp[i + 1][comb], dp[i][comb])
        return dp[n][(1 << 8) - 1]
    
    appear = [False for _ in range(8)]
    for c in a:
        appear[c] = True
    
    result = 0
    for c in appear:
        result += int(c)
    
    cur = 0
    for lev in range(9, -1, -1):
        tpow = 1 << lev
        if cur + tpow < n:
            ret = getLen(cur + tpow)
            if ret != -1:
                result = max(result, ret)
                cur += tpow
    
    return result
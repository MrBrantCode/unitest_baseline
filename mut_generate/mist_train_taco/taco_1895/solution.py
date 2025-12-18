"""
QUESTION:
Each evening Roma plays online poker on his favourite website. The rules of poker on this website are a bit strange: there are always two players in a hand, there are no bets, and the winner takes 1 virtual bourle from the loser.

Last evening Roma started to play poker. He decided to spend no more than k virtual bourles — he will stop immediately if the number of his loses exceeds the number of his wins by k. Also Roma will leave the game if he wins enough money for the evening, i.e. if the number of wins exceeds the number of loses by k.

Next morning Roma found a piece of paper with a sequence on it representing his results. Roma doesn't remember the results exactly, and some characters in the sequence are written in a way such that it's impossible to recognize this character, so Roma can't recall whether he won k bourles or he lost.

The sequence written by Roma is a string s consisting of characters W (Roma won the corresponding hand), L (Roma lost), D (draw) and ? (unknown result). Roma wants to restore any valid sequence by changing all ? characters to W, L or D. The sequence is called valid if all these conditions are met: 

  * In the end the absolute difference between the number of wins and loses is equal to k; 
  * There is no hand such that the absolute difference before this hand was equal to k. 



Help Roma to restore any such sequence.

Input

The first line contains two numbers n (the length of Roma's sequence) and k (1 ≤ n, k ≤ 1000).

The second line contains the sequence s consisting of characters W, L, D and ?. There are exactly n characters in this sequence.

Output

If there is no valid sequence that can be obtained from s by replacing all ? characters by W, L or D, print NO.

Otherwise print this sequence. If there are multiple answers, print any of them.

Examples

Input

3 2
L??


Output

LDL


Input

3 1
W??


Output

NO


Input

20 5
?LLLLLWWWWW?????????


Output

WLLLLLWWWWWWWWLWLWDW
"""

def restore_poker_sequence(n, k, s):
    dp = [[False] * 2010 for _ in range(1001)]
    dp[0][1000] = True  # Adjusted to 1000 to handle negative indices
    
    for i in range(n):
        l = 1000 - k + 1
        r = 1000 + k
        if i == n - 1:
            l -= 1
            r += 1
        for b in range(l, r):
            if s[i] == 'L':
                dp[i + 1][b] = dp[i][b + 1]
            elif s[i] == 'W':
                dp[i + 1][b] = dp[i][b - 1]
            elif s[i] == 'D':
                dp[i + 1][b] = dp[i][b]
            else:
                dp[i + 1][b] = dp[i][b + 1] or dp[i][b - 1] or dp[i][b]
    
    ans = [0] * n
    i = n
    b = -1
    if dp[i][1000 + k]:
        b = 1000 + k
    elif dp[i][1000 - k]:
        b = 1000 - k
    
    if b == -1:
        return 'NO'
    else:
        while i > 0:
            if (s[i - 1] == 'L' or s[i - 1] == '?') and dp[i][b] == dp[i - 1][b + 1]:
                ans[i - 1] = 'L'
                b += 1
            elif (s[i - 1] == 'W' or s[i - 1] == '?') and dp[i][b] == dp[i - 1][b - 1]:
                ans[i - 1] = 'W'
                b -= 1
            else:
                ans[i - 1] = 'D'
            i -= 1
        return ''.join(ans)
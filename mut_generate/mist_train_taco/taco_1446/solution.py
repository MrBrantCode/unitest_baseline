"""
QUESTION:
There are N Snukes lining up in a row. You are given a string S of length N. The i-th Snuke from the front has two red balls if the i-th character in S is `0`; one red ball and one blue ball if the i-th character in S is `1`; two blue balls if the i-th character in S is `2`.

Takahashi has a sequence that is initially empty. Find the number of the possible sequences he may have after repeating the following procedure 2N times, modulo 998244353:

* Each Snuke who has one or more balls simultaneously chooses one of his balls and hand it to the Snuke in front of him, or hand it to Takahashi if he is the first Snuke in the row.
* Takahashi receives the ball and put it to the end of his sequence.

Constraints

* 1 \leq |S| \leq 2000
* S consists of `0`,`1` and `2`.



Note that the integer N is not directly given in input; it is given indirectly as the length of the string S.

Input

Input is given from Standard Input in the following format:


S


Output

Print the number of the possible sequences Takahashi may have after repeating the procedure 2N times, modulo 998244353.

Examples

Input

02


Output

3


Input

1210


Output

55


Input

12001021211100201020


Output

543589959
"""

def count_possible_sequences(S: str) -> int:
    n = len(S)
    mod = 998244353
    
    red = [-1] * (2 * n)
    blue = [-1] * (2 * n)
    cntr = 0
    cntb = 0
    
    for i in range(n):
        cntr = max(cntr, i)
        cntb = max(cntb, i)
        if S[i] == '0':
            red[cntr] = 1
            red[cntr + 1] = 1
            cntr += 2
        elif S[i] == '1':
            red[cntr] = 1
            cntr += 1
            blue[cntb] = 1
            cntb += 1
        elif S[i] == '2':
            blue[cntb] = 1
            blue[cntb + 1] = 1
            cntb += 2
    
    for i in range(1, 2 * n):
        red[i] += red[i - 1]
        blue[i] += blue[i - 1]
    
    dp = [[0] * (4 * n + 5) for _ in range(2 * n + 1)]
    dp[0][0] = 1
    
    for i in range(1, 2 * n + 1):
        for j in range(-blue[i - 1], red[i - 1] + 1, 1):
            dp[i][j] = (dp[i - 1][j + 1] + dp[i - 1][j - 1]) % mod
    
    return dp[-1][red[-1]]
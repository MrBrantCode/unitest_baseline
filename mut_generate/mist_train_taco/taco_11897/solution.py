"""
QUESTION:
Kaavi, the mysterious fortune teller, deeply believes that one's fate is inevitable and unavoidable. Of course, she makes her living by predicting others' future. While doing divination, Kaavi believes that magic spells can provide great power for her to see the future. 

<image>

Kaavi has a string T of length m and all the strings with the prefix T are magic spells. Kaavi also has a string S of length n and an empty string A.

During the divination, Kaavi needs to perform a sequence of operations. There are two different operations:

  * Delete the first character of S and add it at the front of A.
  * Delete the first character of S and add it at the back of A.



Kaavi can perform no more than n operations. To finish the divination, she wants to know the number of different operation sequences to make A a magic spell (i.e. with the prefix T). As her assistant, can you help her? The answer might be huge, so Kaavi only needs to know the answer modulo 998 244 353.

Two operation sequences are considered different if they are different in length or there exists an i that their i-th operation is different. 

A substring is a contiguous sequence of characters within a string. A prefix of a string S is a substring of S that occurs at the beginning of S.

Input

The first line contains a string S of length n (1 ≤ n ≤ 3000).

The second line contains a string T of length m (1 ≤ m ≤ n).

Both strings contain only lowercase Latin letters.

Output

The output contains only one integer — the answer modulo 998 244 353.

Examples

Input


abab
ba


Output


12

Input


defineintlonglong
signedmain


Output


0

Input


rotator
rotator


Output


4

Input


cacdcdbbbb
bdcaccdbbb


Output


24

Note

The first test:

<image>

The red ones are the magic spells. In the first operation, Kaavi can either add the first character "a" at the front or the back of A, although the results are the same, they are considered as different operations. So the answer is 6×2=12.
"""

def count_magic_spell_sequences(S: str, T: str) -> int:
    mod = 998244353
    S = S[::-1]
    NS = len(S)
    NT = len(T)
    
    dp = [[0] * (NT + 1) for _ in range(NS + 1)]
    dp[0][0] = 1
    
    for i in range(NS):
        s = S[i]
        for j in range(NT + 1):
            if j == 0:
                if i != NS - 1:
                    if T[0] == s and dp[i][0]:
                        dp[i + 1][1] = (dp[i + 1][1] + dp[i][0] + min(i, NS - NT)) % mod
                elif T[0] == s and dp[i][0]:
                    dp[i + 1][-1] = (dp[i + 1][-1] + dp[i][0] + NS - NT) % mod
            elif j == NT:
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % mod
            elif i != NS - 1:
                if s == T[j]:
                    dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % mod
            elif s == T[j]:
                dp[i + 1][-1] = (dp[i + 1][-1] + dp[i][j]) % mod
            k = NS - (i - j) - 1
            if k >= NT:
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % mod
            elif T[k] == s:
                if i != NS - 1:
                    dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % mod
                else:
                    dp[i + 1][-1] = (dp[i + 1][-1] + dp[i][j]) % mod
                    if k == 0 and dp[i][j]:
                        dp[i + 1][-1] = (dp[i + 1][-1] + (NS - NT)) % mod
    
    return dp[-1][-1] % mod
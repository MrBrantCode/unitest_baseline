"""
QUESTION:
We say that a binary string (a string containing only characters '0' and '1') is pure if it does not contain either of the strings "0101" or "1010" as a subsequence.
Recall that string T is a subsequence of string S if we can delete some of the letters of S (possibly none) such that the resulting string will become T.
You are given a binary string $S$ with length $N$. We want to make this string pure by deleting some (possibly zero) characters from it. What is the minimum number of characters we have to delete?

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single string $S$ with length $N$.

-----Output-----
For each test case, print a single line containing one integer — the minimum number of characters we have to delete from $S$.

-----Constraints-----
- $1 \le T \le 40$
- $1 \le N \le 1,000$
- $S$ contains only characters '0' and '1'

-----Example Input-----
4
010111101
1011100001011101
0110
111111

-----Example Output-----
2
3
0
0

-----Explanation-----
Example case 1: We can delete the first and third character of our string. There is no way to make the string pure by deleting only one character.
Example case 3: The given string is already pure, so the answer is zero.
"""

def min_deletions_to_make_pure(S: str) -> int:
    dp = [0 if i < 2 else len(S) for i in range(6)]
    
    for c in S:
        if c == '1':
            dp[3] = min(dp[3], dp[0])
            dp[0] += 1
            dp[5] = min(dp[5], dp[2])
            dp[2] += 1
            dp[4] += 1
        else:
            dp[2] = min(dp[2], dp[1])
            dp[1] += 1
            dp[4] = min(dp[4], dp[3])
            dp[3] += 1
            dp[5] += 1
    
    return min(dp)
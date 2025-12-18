"""
QUESTION:
The only difference between the easy and the hard versions is constraints.

A subsequence is a string that can be derived from another string by deleting some or no symbols without changing the order of the remaining symbols. Characters to be deleted are not required to go successively, there can be any gaps between them. For example, for the string "abaca" the following strings are subsequences: "abaca", "aba", "aaa", "a" and "" (empty string). But the following strings are not subsequences: "aabaca", "cb" and "bcaa".

You are given a string $s$ consisting of $n$ lowercase Latin letters.

In one move you can take any subsequence $t$ of the given string and add it to the set $S$. The set $S$ can't contain duplicates. This move costs $n - |t|$, where $|t|$ is the length of the added subsequence (i.e. the price equals to the number of the deleted characters).

Your task is to find out the minimum possible total cost to obtain a set $S$ of size $k$ or report that it is impossible to do so.


-----Input-----

The first line of the input contains two integers $n$ and $k$ ($1 \le n \le 100, 1 \le k \le 10^{12}$) — the length of the string and the size of the set, correspondingly.

The second line of the input contains a string $s$ consisting of $n$ lowercase Latin letters.


-----Output-----

Print one integer — if it is impossible to obtain the set $S$ of size $k$, print -1. Otherwise, print the minimum possible total cost to do it.


-----Examples-----
Input
4 5
asdf

Output
4

Input
5 6
aaaaa

Output
15

Input
5 7
aaaaa

Output
-1

Input
10 100
ajihiushda

Output
233



-----Note-----

In the first example we can generate $S$ = { "asdf", "asd", "adf", "asf", "sdf" }. The cost of the first element in $S$ is $0$ and the cost of the others is $1$. So the total cost of $S$ is $4$.
"""

def minimum_total_cost(n, k, s):
    # Initialize the dp array
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    # Fill the dp array
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            tag = [True] * 26
            for k_idx in range(j, n + 1):
                idx = ord(s[k_idx - 1]) - ord('a')
                if tag[idx]:
                    dp[i][k_idx] += dp[i - 1][j - 1]
                    tag[idx] = False
    
    # Calculate the minimum total cost
    ans = 0
    for i in range(n, -1, -1):
        tmp = sum(dp[i])
        if k > tmp:
            k -= tmp
            ans += (n - i) * tmp
        else:
            ans += k * (n - i)
            k = 0
            break
    
    # If k is still greater than 0, it's impossible
    if k > 0:
        return -1
    
    return ans
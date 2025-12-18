"""
QUESTION:
You are given a string S consisting of a,b and c. Find the number of strings that can be possibly obtained by repeatedly performing the following operation zero or more times, modulo 998244353:
 - Choose an integer i such that 1\leq i\leq |S|-1 and the i-th and (i+1)-th characters in S are different. Replace each of the i-th and (i+1)-th characters in S with the character that differs from both of them (among a, b and c).

-----Constraints-----
 - 2 \leq |S| \leq 2 × 10^5
 - S consists of a, b and c.

-----Input-----
Input is given from Standard Input in the following format:
S

-----Output-----
Print the number of strings that can be possibly obtained by repeatedly performing the operation, modulo 998244353.

-----Sample Input-----
abc

-----Sample Output-----
3

abc, aaa and ccc can be obtained.
"""

def count_possible_strings(S: str) -> int:
    l = len(S)
    if l < 6:
        s = set()
        s.add(S)
        q = [S]
        oa = ord('a')
        while q:
            a = q.pop()
            for i in range(l - 1):
                if a[i] != a[i + 1]:
                    t = chr(oa + 3 - (ord(a[i]) - oa) - (ord(a[i + 1]) - oa))
                    na = a[:i] + t * 2 + a[i + 2:]
                    if na not in s:
                        s.add(na)
                        q.append(na)
        return len(s)
    
    t = S[0] * l
    if t == S:
        return 1
    
    x = 0
    for c in S:
        if c == 'b':
            x += 1
        elif c == 'c':
            x += 2
    
    ans = 0
    if all((S[i] != S[i + 1] for i in range(l - 1))):
        ans += 1
    
    mod = 998244353
    dp = (1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)
    for i in range(l - 1):
        s = (dp[-1] + dp[-2] + dp[-3]) % mod
        dp = ((dp[3] + dp[6]) % mod, (dp[4] + dp[7]) % mod, (dp[5] + dp[8]) % mod, (dp[2] + dp[8]) % mod, (dp[0] + dp[6]) % mod, (dp[1] + dp[7]) % mod, (dp[1] + dp[4]) % mod, (dp[2] + dp[5]) % mod, (dp[0] + dp[3]) % mod, (dp[0] + dp[5] + dp[7] + s) % mod, (dp[1] + dp[3] + dp[8] + s) % mod, (dp[2] + dp[4] + dp[6] + s) % mod)
    
    return (ans + dp[9 + x % 3]) % mod
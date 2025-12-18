"""
QUESTION:
You have multiset of n strings of the same length, consisting of lowercase English letters. We will say that those strings are easy to remember if for each string there is some position i and some letter c of the English alphabet, such that this string is the only string in the multiset that has letter c in position i.

For example, a multiset of strings {"abc", "aba", "adc", "ada"} are not easy to remember. And multiset {"abc", "ada", "ssa"} is easy to remember because:   the first string is the only string that has character c in position 3;  the second string is the only string that has character d in position 2;  the third string is the only string that has character s in position 2. 

You want to change your multiset a little so that it is easy to remember. For a_{ij} coins, you can change character in the j-th position of the i-th string into any other lowercase letter of the English alphabet. Find what is the minimum sum you should pay in order to make the multiset of strings easy to remember.


-----Input-----

The first line contains two integers n, m (1 ≤ n, m ≤ 20) — the number of strings in the multiset and the length of the strings respectively. Next n lines contain the strings of the multiset, consisting only of lowercase English letters, each string's length is m.

Next n lines contain m integers each, the i-th of them contains integers a_{i}1, a_{i}2, ..., a_{im} (0 ≤ a_{ij} ≤ 10^6).


-----Output-----

Print a single number — the answer to the problem.


-----Examples-----
Input
4 5
abcde
abcde
abcde
abcde
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1

Output
3

Input
4 3
abc
aba
adc
ada
10 10 10
10 1 10
10 10 10
10 1 10

Output
2

Input
3 3
abc
ada
ssa
1 1 1
1 1 1
1 1 1

Output
0
"""

def min_cost_to_make_easy_to_remember(n, m, strings, costs):
    s = []
    for i in range(n):
        s.append(list(map(lambda x: ord(x) - 97, list(strings[i]))))
    
    mc = [[0 for _ in range(22)] for _ in range(22)]
    c = [[0 for _ in range(22)] for _ in range(22)]
    maxmask = 1 << n
    maxx = 10 ** 8
    dp = [maxx for _ in range(maxmask)]
    
    for i in range(n):
        for j in range(m):
            mx = 0
            for k in range(n):
                if s[i][j] == s[k][j]:
                    mc[i][j] |= 1 << k
                    c[i][j] += costs[k][j]
                    mx = max(mx, costs[k][j])
            c[i][j] -= mx
    
    dp[0] = 0
    for i in range(1, maxmask):
        for j in range(n):
            if i & 1 << j:
                lb = j
                break
        mask = i
        for j in range(m):
            dp[mask] = min(dp[mask], dp[mask ^ 1 << lb] + costs[lb][j], dp[mask & (mask ^ mc[lb][j])] + c[lb][j])
    
    return dp[(1 << n) - 1]
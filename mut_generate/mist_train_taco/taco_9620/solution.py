"""
QUESTION:
A string with length $L$ is called rich if $L \ge 3$ and there is a character which occurs in this string strictly more than $L/2$ times.
You are given a string $S$ and you should answer $Q$ queries on this string. In each query, you are given a substring $S_L, S_{L+1}, \ldots, S_R$. Consider all substrings of this substring. You have to determine whether at least one of them is rich.

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $Q$.
- The second line contains a single string $S$ with length $N$.
- Each of the next $Q$ lines contains two space-separated integers $L$ and $R$ describing a query.

-----Output-----
For each query, print a single line containing the string "YES" if the given substring contains a rich substring or "NO" if it does not contain any rich substring.

-----Constraints-----
- $1 \le T \le 10$
- $1 \le N, Q \le 10^5$
- $1 \le L \le R \le N$
- $S$ contains only lowercase English letters

-----Example Input-----
1
10 2
helloworld
1 3
1 10

-----Example Output-----
NO
YES
"""

from bisect import bisect_left

def is_rich_substring_present(S, queries):
    n = len(S)
    index = []
    
    # Preprocess the string to find all indices where rich substrings start
    for i in range(n - 2):
        dictt = {}
        for j in S[i:i + 3]:
            if j in dictt:
                dictt[j] += 1
            else:
                dictt[j] = 1
        if max(dictt.values()) >= 2:
            index.append(i + 1)
    
    results = []
    
    # Process each query
    for (l, r) in queries:
        ind = bisect_left(index, l)
        if ind == len(index):
            results.append('NO')
        elif index[ind] + 2 <= r:
            results.append('YES')
        else:
            results.append('NO')
    
    return results
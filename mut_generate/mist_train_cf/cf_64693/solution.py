"""
QUESTION:
Given a string `s` and a list of queries `queries`, where each query is a list `[left, right, k]`, determine if the substring `s[left..right]` can be transformed into a palindrome by rearranging the characters and replacing up to `k` characters with any lowercase English letter.

`1 <= s.length, queries.length <= 10^5`
`0 <= queries[i][0] <= queries[i][1] < s.length`
`0 <= queries[i][2] <= s.length`
`s` only contains lowercase English letters.

Create a function `can_make_pali_queries(s, queries)` that returns a list of boolean values, where the `i`-th value corresponds to the result of the `i`-th query.
"""

def can_make_pali_queries(s, queries):
    prefix_sum = [[0]*26]
    for ch in s:
        new = prefix_sum[-1][:]
        new[ord(ch) - ord('a')] += 1
        prefix_sum.append(new)
    res = []
    for left, right, k in queries:
        odd_counts = sum((prefix_sum[right+1][i] - (prefix_sum[left][i] if left > 0 else 0)) % 2 for i in range(26))
        res.append(odd_counts // 2 <= k)
    
    return res
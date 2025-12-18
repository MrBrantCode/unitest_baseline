"""
QUESTION:
Given a 2D integer matrix `queries` where each `queries[i] = [ni, ki]`, determine the count of unique methods to insert positive integers into an array of length `ni` such that the multiplication of the integers equals `ki`. The response to the `ith` query is the count of methods modulo `10^9 + 7`. Write a function `waysToFillArray(queries)` to return an integer matrix `answer` where `answer.length == queries.length`, and `answer[i]` is the response to the `ith` query.

Constraints: 
`1 <= queries.length <= 10^4`
`1 <= ni, ki <= 10^4`
"""

prime = [0, 0] + [1] * 10000
p, MOD = [], 10 ** 9 + 7
for i in range(2, int(10000 ** .5) + 1):
    if prime[i]:
        prime[i * i: 10001: i] = [0] * len(prime[i * i: 10001: i])
for i in range(10001):
    if prime[i]:
        p.append(i)

c = [[0] * 10001 for _ in range(14)]
for i in range(13):
    c[i][0] = 1
for i in range(1, 10001):
    c[0][i] = 2
for i in range(1, 13):
    for j in range(1, 10001):
        c[i][j] = (c[i - 1][j] + c[i][j - 1]) % MOD

def waysToFillArray(queries):
    ans, d = [1] * len(queries), [0] * len(queries)
    for i in range(len(queries)):
        n, k = queries[i]
        for j in p:
            while k % j == 0:
                k //= j
                d[i] += 1
            if j > k ** .5 + 1:
                break
        if prime[k]:
            d[i] += 1
        if d[i] > n - 1 or n > k:
            ans[i] = 0
        else:
            ans[i] = c[d[i] - 1][n - 1]
    return ans
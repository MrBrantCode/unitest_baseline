"""
QUESTION:
For an array b of length m we define the function f as 

 f(b) = \begin{cases} b[1] &   if  m = 1 \\\ f(b[1] ⊕ b[2],b[2] ⊕ b[3],...,b[m-1] ⊕ b[m]) &   otherwise, \end{cases}  

where ⊕ is [bitwise exclusive OR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).

For example, f(1,2,4,8)=f(1⊕2,2⊕4,4⊕8)=f(3,6,12)=f(3⊕6,6⊕12)=f(5,10)=f(5⊕10)=f(15)=15

You are given an array a and a few queries. Each query is represented as two integers l and r. The answer is the maximum value of f on all continuous subsegments of the array a_l, a_{l+1}, …, a_r.

Input

The first line contains a single integer n (1 ≤ n ≤ 5000) — the length of a.

The second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ 2^{30}-1) — the elements of the array.

The third line contains a single integer q (1 ≤ q ≤ 100 000) — the number of queries.

Each of the next q lines contains a query represented as two integers l, r (1 ≤ l ≤ r ≤ n).

Output

Print q lines — the answers for the queries.

Examples

Input

3
8 4 1
2
2 3
1 2


Output

5
12


Input

6
1 2 4 8 16 32
4
1 6
2 5
3 4
1 2


Output

60
30
12
3

Note

In first sample in both queries the maximum value of the function is reached on the subsegment that is equal to the whole segment.

In second sample, optimal segment for first query are [3,6], for second query — [2,5], for third — [3,4], for fourth — [1,2].
"""

def max_f_on_subsegments(a, queries):
    n = len(a)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    # Initialize the dp array
    for i in range(n):
        dp[0][i] = a[i]
    
    # Fill the dp array with XOR values
    for i in range(1, n):
        for j in range(0, n - i + 1):
            dp[i][j] = dp[i - 1][j + 1] ^ dp[i - 1][j]
    
    # Update the dp array to store the maximum values
    for i in range(1, n):
        for j in range(0, n - i):
            dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i - 1][j + 1])
    
    # Process each query and store the results
    results = []
    for l, r in queries:
        l -= 1  # Convert to 0-based index
        results.append(dp[r - l - 1][l])
    
    return results
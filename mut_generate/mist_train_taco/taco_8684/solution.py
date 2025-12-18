"""
QUESTION:
Unfortunately someone has come and eaten the problem statement. Are you good enough to solve it without the statement?

Input
The first line contains T denoting the number of test cases.
The next  T lines describe test cases and contain two integers each: N and M.

Output
For each test case output one integer - answer for the question.

Constraints
T ≤ 1000
1 ≤ N, M ≤ 10^9

Note:
N, M ≤ 1000 for 30% of the test

SAMPLE INPUT
6
28 1
39 1
90 1
15 2
123 2
114514 1919

SAMPLE OUTPUT
68
90
81
40
17
16
"""

def calculate_test_case_result(N, M):
    # Helper function to calculate the sum of squares of digits
    def go(x):
        s = str(x)
        res = 0
        for i in s:
            res += int(i) * int(i)
        return res
    
    # Precompute the up array
    up = [[0 for _ in range(1000)] for _ in range(30)]
    
    for i in range(1000):
        up[0][i] = go(i)
    
    for i in range(1, 30):
        for j in range(1000):
            up[i][j] = up[i-1][up[i-1][j]]
    
    # Calculate the result for the given test case
    n = go(N)
    M -= 1
    for i in range(30):
        if (M & (1 << i)):
            n = up[i][n]
    
    return n
"""
QUESTION:
Programmers working on a large project have just received a task to write exactly m lines of code. There are n programmers working on a project, the i-th of them makes exactly ai bugs in every line of code that he writes. 

Let's call a sequence of non-negative integers v1, v2, ..., vn a plan, if v1 + v2 + ... + vn = m. The programmers follow the plan like that: in the beginning the first programmer writes the first v1 lines of the given task, then the second programmer writes v2 more lines of the given task, and so on. In the end, the last programmer writes the remaining lines of the code. Let's call a plan good, if all the written lines of the task contain at most b bugs in total.

Your task is to determine how many distinct good plans are there. As the number of plans can be large, print the remainder of this number modulo given positive integer mod.

Input

The first line contains four integers n, m, b, mod (1 ≤ n, m ≤ 500, 0 ≤ b ≤ 500; 1 ≤ mod ≤ 109 + 7) — the number of programmers, the number of lines of code in the task, the maximum total number of bugs respectively and the modulo you should use when printing the answer.

The next line contains n space-separated integers a1, a2, ..., an (0 ≤ ai ≤ 500) — the number of bugs per line for each programmer.

Output

Print a single integer — the answer to the problem modulo mod.

Examples

Input

3 3 3 100
1 1 1


Output

10


Input

3 6 5 1000000007
1 2 3


Output

0


Input

3 5 6 11
1 2 1


Output

0
"""

def count_good_plans(n, m, b, mod, bugs_per_line):
    # Initialize the dp array
    dp = [[[0 for _ in range(b + 1)] for _ in range(m + 1)] for _ in range(2)]
    
    # Base case: when no lines are written, there is exactly one way to achieve 0 bugs
    for i in range(n + 1):
        for x in range(b + 1):
            dp[i % 2][0][x] = 1
    
    # Fill the dp array
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for x in range(b + 1):
                if bugs_per_line[i - 1] <= x:
                    dp[i % 2][j][x] = (dp[(i - 1) % 2][j][x] + dp[i % 2][j - 1][x - bugs_per_line[i - 1]]) % mod
                else:
                    dp[i % 2][j][x] = dp[(i - 1) % 2][j][x] % mod
    
    # The answer is the number of ways to write m lines with at most b bugs
    return dp[n % 2][m][b]
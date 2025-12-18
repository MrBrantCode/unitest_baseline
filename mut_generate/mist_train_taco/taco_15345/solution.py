"""
QUESTION:
There are n students living in the campus. Every morning all students wake up at the same time and go to wash. There are m rooms with wash basins. The i-th of these rooms contains ai wash basins. Every student independently select one the rooms with equal probability and goes to it. After all students selected their rooms, students in each room divide into queues by the number of wash basins so that the size of the largest queue is the least possible. Calculate the expected value of the size of the largest queue among all rooms.

Input

The first line contains two positive integers n and m (1 ≤ n, m ≤ 50) — the amount of students and the amount of rooms. The second line contains m integers a1, a2, ... , am (1 ≤ ai ≤ 50). ai means the amount of wash basins in the i-th room.

Output

Output single number: the expected value of the size of the largest queue. Your answer must have an absolute or relative error less than 10 - 9.

Examples

Input

1 1
2


Output

1.00000000000000000000


Input

2 2
1 1


Output

1.50000000000000000000


Input

2 3
1 1 1


Output

1.33333333333333350000


Input

7 5
1 1 2 3 1


Output

2.50216960000000070000
"""

def calculate_largest_queue_expected_value(n, m, wash_basins):
    MAX_N = 55
    ncr = [[0 for i in range(MAX_N)] for j in range(MAX_N)]
    ncr[0][0] = 1
    for i in range(1, MAX_N):
        ncr[i][0] = 1
        for j in range(1, MAX_N):
            ncr[i][j] = ncr[i - 1][j - 1] + ncr[i - 1][j]
    
    upto = [0 for i in range(MAX_N)]
    for i in range(1, MAX_N):
        dp = [[0 for j in range(MAX_N)] for k in range(MAX_N)]
        dp[0][0] = 1
        for j in range(m):
            for k in range(0, min(n, i * wash_basins[j]) + 1):
                for l in range(0, n - k + 1):
                    dp[j + 1][k + l] += dp[j][l] * ncr[n - l][k]
        upto[i] = dp[m][n]
    
    ans = 0
    for i in range(1, MAX_N):
        ans += (upto[i] - upto[i - 1]) * i
    
    return ans / (m ** n)
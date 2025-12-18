"""
QUESTION:
N people run a marathon. There are M resting places on the way. For each resting place, the i-th runner takes a break with probability P_i percent. When the i-th runner takes a break, he gets rest for T_i time.

The i-th runner runs at constant speed V_i, and the distance of the marathon is L.

You are requested to compute the probability for each runner to win the first place. If a runner arrives at the goal with another person at the same time, they are not considered to win the first place.



Input

A dataset is given in the following format:

N M L
P_1 T_1 V_1
P_2 T_2 V_2
...
P_N T_N V_N


The first line of a dataset contains three integers N (1 \leq N \leq 100), M (0 \leq M \leq 50) and L (1 \leq L \leq 100,000). N is the number of runners. M is the number of resting places. L is the distance of the marathon.

Each of the following N lines contains three integers P_i (0 \leq P_i \leq 100), T_i (0 \leq T_i \leq 100) and V_i (0 \leq V_i \leq 100) describing the i-th runner. P_i is the probability to take a break. T_i is the time of resting. V_i is the speed.

Output

For each runner, you should answer the probability of winning. The i-th line in the output should be the probability that the i-th runner wins the marathon. Each number in the output should not contain an error greater than 10^{-5}.

Examples

Input

2 2 50
30 50 1
30 50 2


Output

0.28770000
0.71230000


Input

2 1 100
100 100 10
0 100 1


Output

0.00000000
1.00000000


Input

3 1 100
50 1 1
50 1 1
50 1 1


Output

0.12500000
0.12500000
0.12500000


Input

2 2 50
30 0 1
30 50 2


Output

0.51000000
0.49000000
"""

import bisect

def nCr(n, r):
    r = min(r, n - r)
    numerator = 1
    for i in range(n, n - r, -1):
        numerator *= i
    denominator = 1
    for i in range(r, 1, -1):
        denominator *= i
    return numerator // denominator

def calculate_win_probabilities(N, M, L, runners):
    data = [[0 for i in range(M + 1)] for i in range(N)]
    
    for i in range(N):
        p, t, v = runners[i]
        for j in range(M + 1):
            data[i][j] = (t * j + L / v if v != 0 else 9999999999999999, 
                          (p / 100.0) ** j * nCr(M, j) * (1 - p / 100.0) ** (M - j))
    
    ans = []
    for i in range(N):
        win = 0
        for j in range(M + 1):
            wintmp = data[i][j][1]
            for x in range(N):
                if i == x:
                    continue
                tmp = 0
                for a, b in data[x][bisect.bisect_right(data[x], (data[i][j][0], 5)):]:
                    tmp += b
                wintmp *= tmp
            win += wintmp
        ans.append(win)
    
    return ans
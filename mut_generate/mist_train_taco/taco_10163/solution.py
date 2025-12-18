"""
QUESTION:
N players will participate in a tennis tournament. We will call them Player 1, Player 2, \ldots, Player N.
The tournament is round-robin format, and there will be N(N-1)/2 matches in total.
Is it possible to schedule these matches so that all of the following conditions are satisfied? If the answer is yes, also find the minimum number of days required.
 - Each player plays at most one matches in a day.
 - Each player i (1 \leq i \leq N) plays one match against Player A_{i, 1}, A_{i, 2}, \ldots, A_{i, N-1} in this order.

-----Constraints-----
 - 3 \leq N \leq 1000
 - 1 \leq A_{i, j} \leq N
 - A_{i, j} \neq i
 - A_{i, 1}, A_{i, 2}, \ldots, A_{i, N-1} are all different.

-----Input-----
Input is given from Standard Input in the following format:
N
A_{1, 1} A_{1, 2} \ldots A_{1, N-1}
A_{2, 1} A_{2, 2} \ldots A_{2, N-1}
:
A_{N, 1} A_{N, 2} \ldots A_{N, N-1}

-----Output-----
If it is possible to schedule all the matches so that all of the conditions are satisfied, print the minimum number of days required; if it is impossible, print -1.

-----Sample Input-----
3
2 3
1 3
1 2

-----Sample Output-----
3

All the conditions can be satisfied if the matches are scheduled for three days as follows:
 - Day 1: Player 1 vs Player 2
 - Day 2: Player 1 vs Player 3
 - Day 3: Player 2 vs Player 3
This is the minimum number of days required.
"""

from collections import deque

def calculate_minimum_days(n, matches):
    l = [[int(i) - 1 for i in player_matches] for player_matches in matches]
    q = deque(list(range(n)))
    days = [0 for i in range(n)]
    pairs = [-1 for i in range(n)]
    
    while q:
        a = q.popleft()
        if len(l[a]) == 0:
            continue
        b = l[a].pop(0)
        if pairs[b] == a:
            days[a] = days[b] = max(days[a], days[b]) + 1
            q.append(a)
            q.append(b)
        else:
            pairs[a] = b
    
    return max(days) if not any(l) else -1
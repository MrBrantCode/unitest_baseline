"""
QUESTION:
There is an infinitely long street that runs west to east, which we consider as a number line.
There are N roadworks scheduled on this street.
The i-th roadwork blocks the point at coordinate X_i from time S_i - 0.5 to time T_i - 0.5.
Q people are standing at coordinate 0. The i-th person will start the coordinate 0 at time D_i, continue to walk with speed 1 in the positive direction and stop walking when reaching a blocked point.
Find the distance each of the Q people will walk.

-----Constraints-----
 - All values in input are integers.
 - 1 \leq N, Q \leq 2 \times 10^5
 - 0 \leq S_i < T_i \leq 10^9
 - 1 \leq X_i \leq 10^9
 - 0 \leq D_1 < D_2 < ... < D_Q \leq 10^9
 - If i \neq j and X_i = X_j, the intervals [S_i, T_i) and [S_j, T_j) do not overlap.

-----Input-----
Input is given from Standard Input in the following format:
N Q
S_1 T_1 X_1
:
S_N T_N X_N
D_1
:
D_Q

-----Output-----
Print Q lines. The i-th line should contain the distance the i-th person will walk or -1 if that person walks forever.

-----Sample Input-----
4 6
1 3 2
7 13 10
18 20 13
3 4 2
0
1
2
3
5
8

-----Sample Output-----
2
2
10
-1
13
-1

The first person starts coordinate 0 at time 0 and stops walking at coordinate 2 when reaching a point blocked by the first roadwork at time 2.
The second person starts coordinate 0 at time 1 and reaches coordinate 2 at time 3. The first roadwork has ended, but the fourth roadwork has begun, so this person also stops walking at coordinate 2.
The fourth and sixth persons encounter no roadworks while walking, so they walk forever. The output for these cases is -1.
"""

import heapq
from collections import defaultdict

def calculate_walking_distances(N, Q, roadworks, start_times):
    INF = 1 << 31
    event = []
    
    # Create events for roadworks
    for s, t, x in roadworks:
        event.append((s - x, -1, x))
        event.append((t - x, 0, x))
    
    # Create events for people
    for i, d in enumerate(start_times):
        event.append((d, 1, i))
    
    # Initialize answer list
    ans = [-1] * Q
    
    # Sort events
    event.sort()
    
    # Priority queue and counters
    q = []
    push = defaultdict(int)
    pop = defaultdict(int)
    
    # Process events
    for t, typ, x in event:
        if typ == -1:
            heapq.heappush(q, x)
            push[x] += 1
        elif typ == 0:
            pop[x] += 1
        else:
            p = -1
            if q:
                p = q[0]
            while p != -1 and push[p] - pop[p] == 0:
                heapq.heappop(q)
                if q:
                    p = q[0]
                else:
                    p = -1
                    break
            ans[x] = p
    
    return ans
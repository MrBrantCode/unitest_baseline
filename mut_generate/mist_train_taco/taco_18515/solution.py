"""
QUESTION:
There are N persons called Person 1 through Person N.
You are given M facts that "Person A_i and Person B_i are friends." The same fact may be given multiple times.
If X and Y are friends, and Y and Z are friends, then X and Z are also friends. There is no friendship that cannot be derived from the M given facts.
Takahashi the evil wants to divide the N persons into some number of groups so that every person has no friend in his/her group.
At least how many groups does he need to make?

-----Constraints-----
 - 2 \leq N \leq 2\times 10^5
 - 0 \leq M \leq 2\times 10^5
 - 1\leq A_i,B_i\leq N
 - A_i \neq B_i

-----Input-----
Input is given from Standard Input in the following format:
N M
A_1 B_1
\vdots
A_M B_M

-----Output-----
Print the answer.

-----Sample Input-----
5 3
1 2
3 4
5 1

-----Sample Output-----
3

Dividing them into three groups such as \{1,3\}, \{2,4\}, and \{5\} achieves the goal.
"""

from collections import deque

def minimum_groups_needed(N, M, friendships):
    # Initialize the graph and visited list
    g = {i: set() for i in range(N)}
    v = [-1 for i in range(N)]
    
    # Build the graph from the friendships
    for (a, b) in friendships:
        g[a - 1].add(b - 1)
        g[b - 1].add(a - 1)
    
    # Initialize the queue and answer
    Q = deque()
    ans = 0
    
    # Perform BFS to find the largest connected component
    for a in range(N):
        if v[a] == -1:
            v[a] = 1
            ans_tmp = 1
            Q.append(a)
            while len(Q) > 0:
                na = Q.popleft()
                for nb in g[na]:
                    if v[nb] == -1:
                        v[nb] = 1
                        ans_tmp += 1
                        Q.append(nb)
            ans = max(ans, ans_tmp)
    
    return ans
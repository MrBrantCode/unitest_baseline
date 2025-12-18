"""
QUESTION:
You are a programmer who loves bishojo games (a sub-genre of dating simulation games). A game, which is titled "I * C * P * C!" and was released yesterday, has arrived to you just now. This game has multiple endings. When you complete all of those endings, you can get a special figure of the main heroine, Sakuya. So, you want to hurry and play the game! But, let's calm down a bit and think how to complete all of the endings in the shortest time first.

In fact, you have a special skill that allows you to know the structure of branching points of games. By using the skill, you have found out that all of the branching points in this game are to select two choices "Yes" or "No", and once a different choice is taken the branched stories flow to different endings; they won't converge any more, like a binary tree. You also noticed that it takes exactly one minute to proceed the game from a branching point to another branching point or to an ending. In addition, you can assume it only takes negligible time to return to the beginning of the game (``reset'') and to play from the beginning to the first branching point.

The game has an additional feature called "Quick Save", which can significantly reduce the playing time for completion. The feature allows you to record the point where you are currently playing and return there at any time later. You can record any number of times, but you can hold only the last recorded point. That is, when you use Quick Save, you overwrite the previous record. If you want to return to the overwritten point, you must play the game from the beginning once again.

Well, let's estimate how long it will take for completing all of the endings in the shortest time.



Input

A data set is given in the following format.

The first line of the data set contains one integer N (2 \leq N \leq 500{,}000), which denotes the number of the endings in this game. The following N-1 lines describe the branching points. The i-th line describes the branching point of ID number i and contains two integers Yes_i and No_i (i + 1 \leq Yes_i, No_i \leq N), which denote the ID numbers of the next branching points when you select Yes or No respectively. Yes_i = N means that you can reach an ending if you select Yes, and so for No_i = N. The branching point with ID 1 is the first branching point. The branching points with ID between 2 and N-1 (inclusive) appear exactly once in Yes_i's and No_i's.

Output

Print the shortest time in a line.

Examples

Input

4
2 3
4 4
4 4


Output

6


Input

5
5 2
3 5
5 4
5 5


Output

8
"""

from collections import deque

def calculate_shortest_time(N, branching_points):
    A = [0] * (N - 1)
    B = [0] * (N - 1)
    
    for i in range(N - 1):
        a, b = branching_points[i]
        if not a <= b:
            a, b = b, a
        A[i] = a - 1
        B[i] = b - 1
    
    que = deque([0])
    vs = []
    dist = [0] * (N - 1)
    
    while que:
        v = que.popleft()
        vs.append(v)
        d = dist[v]
        if A[v] != N - 1:
            w = A[v]
            que.append(w)
            dist[w] = d + 1
        if B[v] != N - 1:
            w = B[v]
            que.append(w)
            dist[w] = d + 1
    
    sz = [0] * (N - 1)
    dp = [[0, 0] for _ in range(N - 1)]
    vs.reverse()
    
    for v in vs:
        a = A[v]
        b = B[v]
        if a == N - 1:
            dp[v][0] = 2
            dp[v][1] = dist[v] + 2
            sz[v] = 2
        elif b == N - 1:
            dp[v][0] = dp[a][0] + sz[a] + 1
            dp[v][1] = dp[a][1] + 1
            sz[v] = sz[a] + 1
        else:
            dp[v][0] = dp[a][0] + dp[b][0] + sz[a] + sz[b]
            dp[v][1] = min(dp[a][0] + dp[b][1] + sz[a], dp[a][1] + dp[b][0] + sz[b], dp[a][1] + dp[b][1])
            sz[v] = sz[a] + sz[b]
    
    return dp[0][1]
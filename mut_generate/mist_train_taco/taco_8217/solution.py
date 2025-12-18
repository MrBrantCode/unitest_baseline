"""
QUESTION:
The director of your college is planning to send 2 people to the ICPC regionals. He wants them to be from different branches. You will be given a list of pairs of student ids. Each pair is made of students from the same branch. Determine how many pairs of students from different branches they can choose from.
Example 1:
Input:
N=5
P=3
pairs[]={{0,1},
         {2,3},
         {0,4}}
Output:
6
Explanation:
Their are total five studets 0,1,2,3,4.
Students [0,1,4] are from same bracnh while 
[2,3] are from a different one.So we can choose
different pairs like: [0,2],[0,3],[1,2],[1,3],
[4,2],[4,3]
 
Example 2:
Input:
N=4 
P=1
pairs[]={{0,2}}
Output:
5
Explanation:
[0,1],[0,3],[2,1],[2,3] and [1,3] are all possible 
pairs because [0,2],[1] and [3] all belongs to 
different branches.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function numberOfPairs() which takes the 2d array pairs[], its size P and an integer N representing total number of students as input parameters and returns the total number of pairs(as explianed in the question)..
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraint:
1<=N<=10^{5}
1<=P<=10^{4}
0<=P[i][0],P[i][1]
"""

from typing import List
from collections import deque

def count_pairs_from_different_branches(N: int, P: int, pairs: List[List[int]]) -> int:
    visit = [0] * N
    adj = [[] for _ in range(N)]
    
    for pair in pairs:
        adj[pair[0]].append(pair[1])
        adj[pair[1]].append(pair[0])

    def bfs(u: int) -> int:
        visit[u] = 1
        q = deque([u])
        count = 0
        while q:
            t = q.popleft()
            count += 1
            for neighbor in adj[t]:
                if visit[neighbor] == 0:
                    visit[neighbor] = 1
                    q.append(neighbor)
        return count

    total_pairs = 0
    for i in range(N):
        if visit[i] == 0:
            component_size = bfs(i)
            total_pairs += component_size * (N - component_size)
    
    return total_pairs // 2
"""
QUESTION:
Captain America is hiding from Thanos in a maze full of N rooms connected by M gates.
The maze is designed in such a way that each room leads to another room via gates. All connecting gates are unidirectional. Captain America is hiding only in those rooms which are accessible directly/indirectly through every other room in the maze.
Help Thanos find the number of rooms in which Captain America can hide. 
 
Example 1:
Input:
N = 5 and M = 5
V = [[1, 2], [2, 3], [3, 4], [4, 3], [5, 4]]
Output: 2
Explanation:
We can look closesly after forming graph 
than captain america only can hide in a 
room 3 and 4 because they are the only room 
which have gates through them. So,
answer is 2.
Example 2:
Input:
N = 2, M = 1
V = [[1, 2]]
Output: 1
Your Task:  
You don't need to read input or print anything. Your task is to complete the function captainAmerica() which takes the integer N, an integer M and 2-d array V as input parameters and returns the Total no of rooms.
Expected Time Complexity: O(N+M)
Expected Auxiliary Space: O(N+M)
 
Constraints:
1 ≤ n ≤ 30000
1 ≤ m ≤ 200000
1 ≤ p,q ≤ n
"""

from collections import Counter, deque

class UF:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]

    def find(self, k):
        ok = k
        while self.parent[k] != k:
            k = self.parent[k]
        while self.parent[ok] != k:
            pk = self.parent[ok]
            self.parent[ok] = k
            ok = pk
        return k

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        self.parent[x] = py

    def getStart(self):
        cnt = Counter()
        for k in range(self.n):
            cnt[self.find(k)] += 1
        for i in range(self.n):
            if cnt[i] == self.n:
                return i
        return -1

def find_captain_america_hiding_rooms(N, M, V):
    v = [[] for _ in range(N)]
    uf = UF(N)
    for edge in V:
        v[edge[0] - 1].append(edge[1] - 1)
        uf.union(edge[0] - 1, edge[1] - 1)
    start = uf.getStart()
    if start == -1:
        return 0
    Q = deque()
    marked = [0 for _ in range(N)]
    marked[start] = 1
    Q.append(start)
    ans = 1
    while len(Q) > 0:
        k = Q.popleft()
        for w in v[k]:
            if not marked[w]:
                ans += 1
                marked[w] = 1
                Q.append(w)
    return ans
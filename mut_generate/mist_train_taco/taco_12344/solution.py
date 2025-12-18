"""
QUESTION:
In Byteland there are N cities, numbered 1 through N. Some pairs of cities are connected by bi-directional roads in such a way that starting from any one city you can visit all other cities either directly or indirectly.

Chef is currently at city A and wants to visit all other cities in Byteland. Chef can only move according to following rule. 

If Chef is at city A then he continues to move from city A to city B, city B to city C (provided A is directly connected to B, B is directly connected to C) and so on unless there are no more cities leading from current city.

If so he jumps back to previous city and repeat the same tour with other cities leading from it which are not visited. Chef repeat this step unless all cities are not visited.

Help Chef to count number of ways in which he can visit all other cities . As this number can be large print it modulo 109+7

-----Input-----
- The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
- The first line of each test case contains a single integer N denoting the number of cities in Byteland.
-  Next N-1 lines contain two space-separated integers u and v denoting there is bi-directional road between city numbered u and v. 
-  Next line contains a single integer A denoting the city number where Chef is present.

-----Output-----
- For each test case, output a single line containing number of ways in which Chef can visit all cities modulo 109+7.

-----Constraints-----
- 1 ≤ T ≤ 5
- 1 ≤ N ≤ 105
- 1 ≤ A ≤ N

-----Subtasks-----
Subtask #1 : (10 points) 
- 1 ≤ N ≤ 5
Subtask #2 : (30 points) 
- 1 ≤ N ≤ 100
Subtask #3 : (60 points) 
- 1 ≤ N ≤ 105

-----Example-----
Input:
2
3
1 2
1 3
1
5
1 2
1 3
2 4
2 5
1

Output:
2
4

-----Explanation-----
Example case 1. Chef can visit cities in two ways according to the problem: 1-2-3 and 1-3-2
Example case 1. Chef can visit cities in four ways according to the problem:

1-2-4-5-3
1-2-5-4-3
1-3-2-4-5
1-3-2-5-4
"""

import sys
sys.setrecursionlimit(10 ** 8)
MOD = 10 ** 9 + 7
fac = [0] * (10 ** 5 + 1)

def pre():
    fac[0] = 1
    for i in range(1, 10 ** 5 + 1):
        fac[i] = fac[i - 1] * i
        fac[i] = fac[i] % MOD

def dfs(gp, vertex, visited, deg, ans):
    visited[vertex] = 1
    stack = []
    stack.append(vertex)
    while len(stack) > 0:
        vertex = stack.pop()
        ans = ans % MOD * fac[deg[vertex]] % MOD
        ans %= MOD
        for i in gp[vertex]:
            if not visited[i]:
                visited[i] = 1
                if vertex in gp[i]:
                    deg[i] -= 1
                stack.append(i)
    return ans % MOD

def count_visit_ways(n, roads, start_city):
    pre()
    deg = [0] * (n + 1)
    gp = [[] for _ in range(n + 1)]
    
    for (a, b) in roads:
        gp[a].append(b)
        gp[b].append(a)
        deg[a] += 1
        deg[b] += 1
    
    visited = [0] * (n + 1)
    return dfs(gp, start_city, visited, deg, 1) % MOD
"""
QUESTION:
Divide and rule

Taro, Hanako, and Jiro rule the JAG Kingdom together. There are N cities in the JAG Kingdom, some of which are connected by two-way roads. You can always reach all the other cities from any city via one or more roads.

One day, Taro and Hanako finally made a mistake and decided to share the city and govern it. However, I don't even like the fact that the city governed by Taro and the city governed by Hanako are directly connected by a single road because they have become so bad. Therefore, we decided to share the governing towns so as to satisfy the following conditions.

* Any pair of towns governed by Taro and Hanako are not directly connected by roads. This is because the relationship between Taro and Hanako is insanely bad.
* Towns governed by the same person are not directly connected by roads. This is to encourage diplomacy by obliging the passage under the control of others.
* The total number of towns governed by Taro and the total number of towns governed by Hanako must be the same. This is because if the total number is not equal, the relationship between Taro and Hanako will be even worse. Here, Mr. Jiro is very open-minded, so the total number of cities governed by Mr. Jiro can be any number.



If the division meets the above conditions, the three people can be convinced to rule, and even if there are no cities governed by someone, there is no complaint. At this time, create a program that enumerates all possible numbers as the total number of cities governed by Mr. Taro (= the total number of cities governed by Mr. Hanako).

Input

The input consists of multiple datasets. The maximum number of datasets is 50. Each data set is represented in the following format.

> N M u1 v1 ... uM vM

The first line consists of two integers N (2 ≤ N ≤ 103) and M (1 ≤ M ≤ 103), which represent the number of cities and the number of roads, respectively. The i-th line of the following M lines consists of two integers ui and vi (1 ≤ ui <vi ≤ N), indicating that the i-th road connects the city ui and the city vi in ​​both directions. Here, it is guaranteed that one city can always reach all other cities via one or more roads. Also, no multiple roads connecting pairs of the same city will be given. That is, (ui, vi) ≠ (uj, vj) is satisfied for all 1 ≤ i <j ≤ M.

The end of the input is represented by a line of two zeros.

Output

For each dataset, if there are K possible total numbers of cities governed by Taro, first output K on the first line, then output the possible total number on each line in ascending order.

Sample Input


6 7
1 2
14
twenty three
twenty five
3 4
4 5
4 6
twenty one
1 2
3 3
1 2
13
twenty three
4 3
1 2
twenty three
3 4
5 4
1 2
twenty three
3 4
4 5
0 0


Output for the Sample Input


2
1
2
0
0
1
1
1
1






Example

Input

6 7
1 2
1 4
2 3
2 5
3 4
4 5
4 6
2 1
1 2
3 3
1 2
1 3
2 3
4 3
1 2
2 3
3 4
5 4
1 2
2 3
3 4
4 5
0 0


Output

2
1
2
0
0
1
1
1
1
"""

def find_possible_governed_cities(N, M, roads):
    if N == 0 and M == 0:
        return []
    
    path = [[False] * N for _ in range(N)]
    for u, v in roads:
        u -= 1
        v -= 1
        path[u][v] = True
        path[v][u] = True
    
    d = [-1] * N
    d[0] = 0
    q = [0]
    
    while q:
        now = q.pop(0)
        for i in range(N):
            if path[now][i] and d[i] == -1:
                q.append(i)
                d[i] = d[now] + 1
    
    ok = True
    for i in range(1, N):
        for j in range(i + 1, N):
            if path[i][j] and d[i] == d[j]:
                ok = False
                break
        if not ok:
            break
    
    if not ok:
        return [0]
    
    num = sum(1 for i in range(N) if d[i] % 2 == 1)
    
    if N % 2 == 1:
        if num % 2 == 1:
            return [1, (N - num) // 2]
        else:
            return [1, num // 2]
    elif num % 2 == 1:
        return [0]
    elif N // 2 == num:
        return [1, num // 2]
    else:
        tmp = min(num, N - num)
        return [2, tmp // 2, (N - tmp) // 2]
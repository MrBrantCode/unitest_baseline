"""
QUESTION:
Navnit is a college student and there are $N$ students in his college .Students are numbered from $1$ to $N$.
You are given $M$ facts that "Student $A_i$ and $B_i$".The same fact can be given multiple times .If $A_i$ is a friend of $B_i$ ,then $B_i$ is also a friend of $A_i$ . If $A_i$ is a friend of $B_i$ and $B_i$ is a friend of $C_i$ then $A_i$ is also a friend of $C_i$.
Find number of ways in which two students can be selected in such a way that they are not friends. 

-----Input:-----
- First line will contain two integers $N$ and $M$. 
- Then $M$ lines follow. Each line contains two integers $A_i$ and $B_i$ denoting the students who are friends.

-----Output:-----
For each testcase, output the number of ways in which  two students can be selected in such a way that they are friends.

-----Constraints-----
- $2 \leq N \leq 200000$
- $0 \leq M \leq 200000$
- $1 \leq A_i,B_i \leq N$

-----Sample Input:-----
5 3
1 2                                                   
3 4
1 5

-----Sample Output:-----
6

-----EXPLANATION:-----
Groups of friend are $[1,2,5]$ and $[3,4]$.Hence the answer is  3 X 2 =6.
"""

from collections import defaultdict

def count_non_friend_pairs(N, M, friendships):
    d = defaultdict(list)
    
    def dfs(i):
        p = 0
        nonlocal v
        e = [i]
        while e:
            p += 1
            x = e.pop(0)
            v[x] = 1
            for friend in d[x]:
                if v[friend] == -1:
                    v[friend] = 1
                    e.append(friend)
        return p
    
    for i in range(1, N + 1):
        d[i] = []
    
    for a, b in friendships:
        d[a].append(b)
        d[b].append(a)
    
    v = [-1] * (N + 1)
    c = 0
    p = []
    
    for i in range(1, N + 1):
        if v[i] == -1:
            c += 1
            p.append(dfs(i))
    
    an = 0
    s = 0
    for i in range(c):
        s += p[i]
        an += p[i] * (N - s)
    
    return an
"""
QUESTION:
A new set of desks just arrived, and it's about time! Things were getting quite cramped in the office. You've been put in charge of creating a new seating chart for the engineers. The desks are numbered, and you sent out a survey to the engineering team asking each engineer the number of the desk they currently sit at, and the number of the desk they would like to sit at (which may be the same as their current desk). Each engineer must either remain where they sit, or move to the desired seat they indicated in the survey. No two engineers currently sit at the same desk, nor may any two engineers sit at the same desk in the new seating arrangement.

How many seating arrangements can you create that meet the specified requirements? The answer may be very large, so compute it modulo 1000000007 = 10^9 + 7.


-----Input-----

Input will begin with a line containing N (1 ≤ N ≤ 100000), the number of engineers. 

N lines follow, each containing exactly two integers. The i-th line contains the number of the current desk of the i-th engineer and the number of the desk the i-th engineer wants to move to. Desks are numbered from 1 to 2·N. It is guaranteed that no two engineers sit at the same desk.


-----Output-----

Print the number of possible assignments, modulo 1000000007 = 10^9 + 7.


-----Examples-----
Input
4
1 5
5 2
3 7
7 3

Output
6

Input
5
1 10
2 10
3 10
4 10
5 5

Output
5



-----Note-----

These are the possible assignments for the first example:   1 5 3 7  1 2 3 7  5 2 3 7  1 5 7 3  1 2 7 3  5 2 7 3
"""

def calculate_seating_arrangements(n, desks):
    m = 2 * n + 1
    u = [[] for _ in range(m)]
    v = [0] * m
    s = [0] * m
    d = 10**9 + 7
    y = 1
    
    for a, b in desks:
        v[a] = b
        if a != b:
            s[b] += 1
            u[b].append(a)
    
    for b in range(m):
        if not v[b]:
            x = 0
            p = [b]
            while p:
                x += 1
                a = p.pop()
                s[a] = -1
                p += u[a]
            y = x * y % d
    
    for a in range(m):
        if s[a] == 0:
            b = v[a]
            while s[b] == 1:
                s[b] = -1
                b = v[b]
            s[b] -= 1
    
    for a in range(m):
        if s[a] == 1:
            y = 2 * y % d
            while s[a]:
                s[a] = 0
                a = v[a]
    
    return y
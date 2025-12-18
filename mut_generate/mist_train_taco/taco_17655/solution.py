"""
QUESTION:
The kingdom of Zion has cities connected by bidirectional roads.  There is a unique path between any pair of cities. Morpheus has found out that the machines are planning to destroy the whole kingdom.  If two machines can join forces, they will attack.  Neo has to destroy roads connecting cities with machines in order to stop them from joining forces.  There must not be any path connecting two machines.

Each of the roads takes an amount of time to destroy, and only one can be worked on at a time.  Given a list of edges and times, determine the minimum time to stop the attack.

For example, there are $n=5$ cities called $\mathbf{0}-4$.  Three of them have machines and are colored red.  The time to destroy is shown next to each road.  If we cut the two green roads, there are no paths between any two machines.  The time required is $3+2=5$.  

Function Description

Complete the function minTime in the editor below.  It must return an integer representing the minimum time to cut off access between the machines.

minTime has the following parameter(s):

roads: a two-dimensional array of integers, each $roads[i]=[city1,city2,time]$ where cities are connected by a road that takes $\textbf{time}$ to destroy  
machines: an array of integers representing cities with machines  

Input Format

The first line of the input contains two space-separated integers, $n$ and $\boldsymbol{\mbox{k}}$, the number of cities and the number of machines.  

Each of the following $n-1$ lines contains three space-separated integers, $\textit{city1},\textit{city2}$, and $\textbf{time}$.  There is a bidirectional road connecting $\text{city1}$ and $\text{city2}$, and to destroy this road it takes $\textbf{time}$ units.

Each of the last $\boldsymbol{\mbox{k}}$ lines contains an integer, $\textit{machine}[i]$, the label of a city with a machine.   

Constraints

$2\leq n\leq10^5$  
$2\leq k\leq n$  
$1\leq time[i]\leq10^6$  

Output Format

Return an integer representing the minimum time required to disrupt the connections among all machines.

Sample Input
5 3
2 1 8
1 0 5
2 4 5
1 3 4
2
4
0

Sample Output
10

Explanation

The machines are located at the cities $0$, $2$ and $4$. Neo can destroy the green roads resulting in a time of $5+5=10$.  Destroying the road between cities $2$ and $1$ instead of between $1$ and $0$ would work, but it's not minimal.
"""

def min_time_to_stop_attack(n, k, roads, machines):
    def leader(x):
        if P[x] == x:
            return P[x]
        if P[x] == x + 10 ** 5:
            return P[x]
        P[x] = leader(P[x])
        return P[x]

    def same(x, y):
        return leader(x) == leader(y)

    def canJoin(x, y):
        return not (leader(x) >= 10 ** 5 and leader(y) >= 10 ** 5)

    def union(x, y):
        a = leader(x)
        b = leader(y)
        if a > b:
            (a, b) = (b, a)
        S[b] += S[a]
        P[a] = b

    lis = sorted(roads, key=lambda x: -x[2])
    P = {x: x for x in range(n)}
    S = {x: 1 for x in range(n)}
    
    for machine in machines:
        P[machine + 10 ** 5] = machine + 10 ** 5
        P[machine] = machine + 10 ** 5
        S[machine + 10 ** 5] = 1
    
    res = 0
    for (x, y, z) in lis:
        if canJoin(x, y):
            union(x, y)
        else:
            res += z
    
    return res
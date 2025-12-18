"""
QUESTION:
Shuseki Kingdom is the world's leading nation for innovation and technology. There are n cities in the kingdom, numbered from 1 to n.

Thanks to Mr. Kitayuta's research, it has finally become possible to construct teleportation pipes between two cities. A teleportation pipe will connect two cities unidirectionally, that is, a teleportation pipe from city x to city y cannot be used to travel from city y to city x. The transportation within each city is extremely developed, therefore if a pipe from city x to city y and a pipe from city y to city z are both constructed, people will be able to travel from city x to city z instantly.

Mr. Kitayuta is also involved in national politics. He considers that the transportation between the m pairs of city (ai, bi) (1 ≤ i ≤ m) is important. He is planning to construct teleportation pipes so that for each important pair (ai, bi), it will be possible to travel from city ai to city bi by using one or more teleportation pipes (but not necessarily from city bi to city ai). Find the minimum number of teleportation pipes that need to be constructed. So far, no teleportation pipe has been constructed, and there is no other effective transportation between cities.

Input

The first line contains two space-separated integers n and m (2 ≤ n ≤ 105, 1 ≤ m ≤ 105), denoting the number of the cities in Shuseki Kingdom and the number of the important pairs, respectively.

The following m lines describe the important pairs. The i-th of them (1 ≤ i ≤ m) contains two space-separated integers ai and bi (1 ≤ ai, bi ≤ n, ai ≠ bi), denoting that it must be possible to travel from city ai to city bi by using one or more teleportation pipes (but not necessarily from city bi to city ai). It is guaranteed that all pairs (ai, bi) are distinct.

Output

Print the minimum required number of teleportation pipes to fulfill Mr. Kitayuta's purpose.

Examples

Input

4 5
1 2
1 3
1 4
2 3
2 4


Output

3


Input

4 6
1 2
1 4
2 3
2 4
3 2
3 4


Output

4

Note

For the first sample, one of the optimal ways to construct pipes is shown in the image below: 

<image>

For the second sample, one of the optimal ways is shown below: 

<image>
"""

def minimum_teleportation_pipes(n, m, pairs):
    n += 1
    cluster = list(range(n))
    dest = [0] * n
    avail = [True] * n
    ab = [[] for _ in range(n)]

    def getroot(x):
        while x != cluster[x]:
            x = cluster[x]
        return x

    def setroot(x, r):
        if r < x != cluster[x]:
            setroot(cluster[x], r)
        cluster[x] = r

    for (a, b) in pairs:
        ab[a].append(b)
        dest[b] += 1
        u, v = getroot(a), getroot(b)
        if u > v:
            u = v
        setroot(a, u)
        setroot(b, u)

    pool = [a for a in range(1, n) if not dest[a]]
    for a in pool:
        for b in ab[a]:
            dest[b] -= 1
            if not dest[b]:
                pool.append(b)

    for a in range(1, n):
        avail[getroot(a)] &= not dest[a]

    return n - sum((f and a == c for (a, c, f) in zip(range(n), cluster, avail)))
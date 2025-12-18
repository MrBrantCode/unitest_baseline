"""
QUESTION:
Girl Lena likes it when everything is in order, and looks for order everywhere. Once she was getting ready for the University and noticed that the room was in a mess — all the objects from her handbag were thrown about the room. Of course, she wanted to put them back into her handbag. The problem is that the girl cannot carry more than two objects at a time, and cannot move the handbag. Also, if he has taken an object, she cannot put it anywhere except her handbag — her inherent sense of order does not let her do so.

You are given the coordinates of the handbag and the coordinates of the objects in some Сartesian coordinate system. It is known that the girl covers the distance between any two objects in the time equal to the squared length of the segment between the points of the objects. It is also known that initially the coordinates of the girl and the handbag are the same. You are asked to find such an order of actions, that the girl can put all the objects back into her handbag in a minimum time period.

Input

The first line of the input file contains the handbag's coordinates xs, ys. The second line contains number n (1 ≤ n ≤ 24) — the amount of objects the girl has. The following n lines contain the objects' coordinates. All the coordinates do not exceed 100 in absolute value. All the given positions are different. All the numbers are integer.

Output

In the first line output the only number — the minimum time the girl needs to put the objects into her handbag. 

In the second line output the possible optimum way for Lena. Each object in the input is described by its index number (from 1 to n), the handbag's point is described by number 0. The path should start and end in the handbag's point. If there are several optimal paths, print any of them. 

Examples

Input

0 0
2
1 1
-1 1


Output

8
0 1 2 0 


Input

1 1
3
4 3
3 4
0 0


Output

32
0 1 2 0 3 0
"""

def minimum_time_to_collect_objects(handbag_coords, object_coords):
    BITS = [1 << sh for sh in range(24)]
    B2N = {v: u for (u, v) in enumerate(BITS)}

    def dist(ptA, ptB):
        return sum(((u - v) ** 2 for (u, v) in zip(ptA, ptB)))

    def getBits(val):
        return tuple(filter(lambda x: x & val, BITS))

    def chooseTwo(pool):
        n = len(pool)
        for i in range(n):
            for j in range(i + 1, n):
                yield (pool[i], pool[j])

    ori = handbag_coords
    pts = object_coords
    N = len(pts)
    vis = set([0])
    mint = [0] + [100000000.0] * (1 << N)
    pres = [None] * (1 << N)
    allb = (1 << N) - 1
    B2P = {BITS[u]: v for (u, v) in enumerate(pts)}
    B2P[0] = ori
    alld = {u: {v: dist(B2P[u], B2P[v]) for v in B2P} for u in B2P}
    getDP = lambda x: mint[x]
    newDist = lambda stt, p: mint[stt] + alld[p[0]][p[1]] + alld[p[0]][0] + alld[p[1]][0]

    for stt in range(1 << N):
        if stt not in vis:
            continue
        bits = getBits(~stt & allb)
        sb = bits[0] if bits else None
        for bit in bits:
            newstt = stt | sb | bit
            nd = newDist(stt, (sb, bit))
            if getDP(newstt) > nd:
                mint[newstt] = nd
                pres[newstt] = sb | bit
                vis.add(newstt)

    minimum_time = mint[allb]
    path = ['0']
    stt = allb
    while stt:
        bits = getBits(pres[stt])
        for bit in bits:
            path.append(str(B2N[bit] + 1))
        path.append('0')
        stt ^= pres[stt]
    optimal_path = ' '.join(path)

    return minimum_time, optimal_path
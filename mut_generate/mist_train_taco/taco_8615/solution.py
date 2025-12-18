"""
QUESTION:
Polycarp lives on a coordinate line at the point $x = 0$. He goes to his friend that lives at the point $x = a$. Polycarp can move only from left to right, he can pass one unit of length each second.

Now it's raining, so some segments of his way are in the rain. Formally, it's raining on $n$ non-intersecting segments, the $i$-th segment which is in the rain is represented as $[l_i, r_i]$ ($0 \le l_i < r_i \le a$).

There are $m$ umbrellas lying on the line, the $i$-th umbrella is located at point $x_i$ ($0 \le x_i \le a$) and has weight $p_i$. When Polycarp begins his journey, he doesn't have any umbrellas.

During his journey from $x = 0$ to $x = a$ Polycarp can pick up and throw away umbrellas. Polycarp picks up and throws down any umbrella instantly. He can carry any number of umbrellas at any moment of time. Because Polycarp doesn't want to get wet, he must carry at least one umbrella while he moves from $x$ to $x + 1$ if a segment $[x, x + 1]$ is in the rain (i.e. if there exists some $i$ such that $l_i \le x$ and $x + 1 \le r_i$).

The condition above is the only requirement. For example, it is possible to go without any umbrellas to a point where some rain segment starts, pick up an umbrella at this point and move along with an umbrella. Polycarp can swap umbrellas while he is in the rain.

Each unit of length passed increases Polycarp's fatigue by the sum of the weights of umbrellas he carries while moving.

Can Polycarp make his way from point $x = 0$ to point $x = a$? If yes, find the minimum total fatigue after reaching $x = a$, if Polycarp picks up and throws away umbrellas optimally.


-----Input-----

The first line contains three integers $a$, $n$ and $m$ ($1 \le a, m \le 2000, 1 \le n \le \lceil\frac{a}{2}\rceil$) — the point at which Polycarp's friend lives, the number of the segments in the rain and the number of umbrellas.

Each of the next $n$ lines contains two integers $l_i$ and $r_i$ ($0 \le l_i < r_i \le a$) — the borders of the $i$-th segment under rain. It is guaranteed that there is no pair of intersecting segments. In other words, for each pair of segments $i$ and $j$ either $r_i < l_j$ or $r_j < l_i$.

Each of the next $m$ lines contains two integers $x_i$ and $p_i$ ($0 \le x_i \le a$, $1 \le p_i \le 10^5$) — the location and the weight of the $i$-th umbrella.


-----Output-----

Print "-1" (without quotes) if Polycarp can't make his way from point $x = 0$ to point $x = a$. Otherwise print one integer — the minimum total fatigue after reaching $x = a$, if Polycarp picks up and throws away umbrellas optimally.


-----Examples-----
Input
10 2 4
3 7
8 10
0 10
3 4
8 1
1 2

Output
14

Input
10 1 1
0 9
0 5

Output
45

Input
10 1 1
0 9
1 5

Output
-1



-----Note-----

In the first example the only possible strategy is to take the fourth umbrella at the point $x = 1$, keep it till the point $x = 7$ (the total fatigue at $x = 7$ will be equal to $12$), throw it away, move on from $x = 7$ to $x = 8$ without an umbrella, take the third umbrella at $x = 8$ and keep it till the end (the total fatigue at $x = 10$ will be equal to $14$). 

In the second example the only possible strategy is to take the first umbrella, move with it till the point $x = 9$, throw it away and proceed without an umbrella till the end.
"""

def minimum_fatigue(a, n, m, rain_segments, umbrellas):
    rainend = set()
    umbr = {}
    keyPointSet = set([0, a])
    
    for l_i, r_i in rain_segments:
        for j in range(l_i + 1, r_i + 1):
            rainend.add(j)
        keyPointSet.add(r_i)
    
    for x_i, p_i in umbrellas:
        if x_i not in umbr or p_i < umbr[x_i]:
            umbr[x_i] = p_i
        keyPointSet.add(x_i)
    
    keyPoint = list(keyPointSet)
    keyPoint.sort()
    
    dp = {}
    dp[0] = {}
    dp[0][0] = 0
    if 0 in umbr:
        dp[0][umbr[0]] = 0
    
    for i in range(1, len(keyPoint)):
        x = keyPoint[i]
        lx = keyPoint[i - 1]
        ifrain = x in rainend
        dp[x] = {}
        nowdp = dp[x]
        lastdp = dp[lx]
        
        for z in lastdp:
            if z == 0:
                if not ifrain:
                    nowdp[0] = lastdp[0]
            else:
                nowdp[z] = lastdp[z] + z * (x - lx)
        
        if len(nowdp) > 0:
            nowdp[0] = min(nowdp.values())
            if x in umbr:
                if umbr[x] not in nowdp or nowdp[0] < nowdp[umbr[x]]:
                    nowdp[umbr[x]] = nowdp[0]
        else:
            return -1
    
    return min(dp[a].values())
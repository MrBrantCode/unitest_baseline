"""
QUESTION:
We have decided to introduce an automatic ticket gate to the railway network of a certain country. One of the difficult issues to implement is determining whether a given ticket can move between designated stations. Each ticket has a boarding station and a getting-off station. With this ticket, you can not only "get on at the boarding station and get off at the getting off station", but you are also allowed to get on and off the train.

There are S stations on this rail network, of which Group R stations are adjacent and can be traversed in both directions without going through other stations. There is only one railroad track connecting adjacent stations. The distance between adjacent stations is the distance measured along this railroad track. There are multiple possible routes from one station to another, depending on the shape of the railway network, but the route with the shortest distance is called the shortest route. If there are multiple such routes, both are accepted as the shortest route.

You can move from station c to station d with a ticket for boarding station a and getting off station b if there is a route p that meets all of the following conditions.

* Route p is the shortest route from station a to station b.
* Route p is a route that starts from station a, goes through station c, then station d, and ends at station b. The section from station c to station d is the shortest route between these two stations.



You will be given route map and ticket information. Next, you will be given several pairs of start and end points, so write a program that determines whether you can move from the start point to the end point with that ticket.



input

The input consists of one dataset. Input data is given in the following format.


S R
u1 v1 w1
u2 v2 w2
::
uR vR wR
a b Q
c1 d1
::
cQ dQ


The numbers given on each line are separated by a single space.

The first line consists of two integers. S (2 ≤ S ≤ 100000) is the number of stations that appear on the railroad map, and R (1 ≤ R ≤ 200000) is the number of pairs of adjacent stations. The following R line is given information on the railroad tracks that directly connect adjacent stations. ui and vi (1 ≤ ui, vi ≤ S) indicate the station numbers at both ends of the i-th line. wi (1 ≤ wi ≤ 1000) is an integer representing the distance between these stations. However, numbers from 1 to S are assigned to each station without duplication, and ui ≠ vi.

The next line consists of three integers. The first two integers represent the ticket sections, where a is the boarding station and b is the getting-off station (1 ≤ a, b ≤ S). The third integer Q (1 ≤ Q ≤ 40000) indicates the number of questions. The question is given on the following Q line. ci and di (1 ≤ ci, di ≤ S) indicate the boarding and alighting stations of the i-th question. However, a ≠ b and ci ≠ di.

output

For each question, print Yes if you can move with the given ticket, or No if you can't.

Example

Input

6 7
1 2 3
1 4 1
2 3 5
4 3 1
3 6 2
4 5 2
5 6 1
1 6 6
1 6
4 3
4 6
5 6
2 6
2 5


Output

Yes
Yes
Yes
Yes
No
No
"""

from heapq import heappush, heappop

def can_move_with_ticket(S, R, edges, a, b, queries):
    # Adjust station indices to be zero-based
    a -= 1
    b -= 1
    
    # Build adjacency list
    adj_list = [[] for _ in range(S)]
    for (u, v, w) in edges:
        u -= 1
        v -= 1
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))
    
    def dijkstra(start):
        INF = 10 ** 20
        dist = [INF] * S
        dist[start] = 0
        parents = [[] for _ in range(S)]
        que = []
        heappush(que, (0, start))
        while que:
            (score, node) = heappop(que)
            for (to, w) in adj_list[node]:
                if dist[to] > score + w:
                    dist[to] = score + w
                    parents[to] = {node}
                    heappush(que, (score + w, to))
                elif dist[to] == score + w:
                    parents[to].add(node)
        return (dist, parents)
    
    def on_shortest_path(c, d, mem):
        if c == d:
            return True
        if d in mem:
            return False
        mem.add(d)
        if dist_from_a[c] >= dist_from_a[d]:
            return False
        for parent in parents[d]:
            if on_shortest_path(c, parent, mem):
                return True
        return False
    
    (dist_from_a, parents) = dijkstra(a)
    (dist_from_b, _) = dijkstra(b)
    shortest = dist_from_a[b]
    
    results = []
    for (c, d) in queries:
        c -= 1
        d -= 1
        if dist_from_a[c] + dist_from_b[c] == shortest and dist_from_a[d] + dist_from_b[d] == shortest and on_shortest_path(c, d, set()):
            results.append('Yes')
        else:
            results.append('No')
    
    return results
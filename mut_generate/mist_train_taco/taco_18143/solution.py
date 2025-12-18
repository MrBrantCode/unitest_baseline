"""
QUESTION:
problem

AOR Ika is at the $ S $ th bus stop at time $ 0 $ and wants to go from there to the $ G $ th bus stop. The number of bus stops $ N $ and $ M $ routes (*) connecting different bus stops are given. The bus stops are numbered $ 1, \ dots, and N $, respectively. Each route consists of $ 4 $ values: origin $ u $, destination $ v $, departure time $ t $, and travel time $ c $. You can catch the bus if you are at the departure $ u $ at the time $ t $ and arrive at the destination $ v $ at the time $ t + c $. While not on the bus, AOR Ika gets wet in the rain. When heading to the $ G $ th bus stop through the route that minimizes the time of getting wet in the rain, output the total time of getting wet in the rain from the time $ 0 $ to the arrival at the $ G $ th bus stop.

(*) In graph theory terms, a path is a sequence of vertices and edges, but please note that it is used here to mean edges.



input

Input is given from standard input in the following format.

$ N \ M \ S \ G $
$ u_1 \ v_1 \ t_1 \ c_1 $
$ \ vdots $
$ u_M \ v_M \ t_M \ c_M $

output

Print the minimum amount of time you get wet in one line. Also, output a line break at the end.

Example

Input

2 2 1 2
1 2 10 100
1 2 5 500


Output

5
"""

from heapq import heappush, heappop

def calculate_minimum_wet_time(N, M, S, G, routes):
    # Adjust indices to be zero-based
    S -= 1
    G -= 1
    
    # Initialize edges list
    edges = [[] for _ in range(N)]
    
    # Populate edges list with routes
    for (u, v, t, c) in routes:
        u -= 1
        v -= 1
        edges[u].append((t, t + c, v))
    
    # Initialize score dictionary and priority queue
    score = {}
    score[(S, 0)] = 0
    que = []
    heappush(que, (0, 0, S))
    
    # Dijkstra's algorithm to find the minimum wet time
    while que:
        (total, time, node) = heappop(que)
        if node == G:
            return total
        
        for (start, end, to) in edges[node]:
            if start < time:
                continue
            new_total = total + (start - time)
            if (to, end) not in score or score[to, end] > new_total:
                score[to, end] = new_total
                heappush(que, (new_total, end, to))
    
    # If no path is found, return -1 (or handle as needed)
    return -1
"""
QUESTION:
There are N cities numbered 1 to N, connected by M railroads.
You are now at City 1, with 10^{100} gold coins and S silver coins in your pocket.
The i-th railroad connects City U_i and City V_i bidirectionally, and a one-way trip costs A_i silver coins and takes B_i minutes.
You cannot use gold coins to pay the fare.
There is an exchange counter in each city. At the exchange counter in City i, you can get C_i silver coins for 1 gold coin.
The transaction takes D_i minutes for each gold coin you give.
You can exchange any number of gold coins at each exchange counter.
For each t=2, ..., N, find the minimum time needed to travel from City 1 to City t. You can ignore the time spent waiting for trains.

-----Constraints-----
 - 2 \leq N \leq 50
 - N-1 \leq M \leq 100
 - 0 \leq S \leq 10^9
 - 1 \leq A_i \leq 50
 - 1 \leq B_i,C_i,D_i \leq 10^9
 - 1 \leq U_i < V_i \leq N
 - There is no pair i, j(i \neq j) such that (U_i,V_i)=(U_j,V_j).
 - Each city t=2,...,N can be reached from City 1 with some number of railroads.
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N M S
U_1 V_1 A_1 B_1
:
U_M V_M A_M B_M
C_1 D_1
:
C_N D_N

-----Output-----
For each t=2, ..., N in this order, print a line containing the minimum time needed to travel from City 1 to City t.

-----Sample Input-----
3 2 1
1 2 1 2
1 3 2 4
1 11
1 2
2 5

-----Sample Output-----
2
14

The railway network in this input is shown in the figure below.
In this figure, each city is labeled as follows:
 - The first line: the ID number i of the city (i for City i)
 - The second line: C_i / D_i
Similarly, each railroad is labeled as follows:
 - The first line: the ID number i of the railroad (i for the i-th railroad in input)
 - The second line: A_i / B_i

You can travel from City 1 to City 2 in 2 minutes, as follows:
 - Use the 1-st railroad to move from City 1 to City 2 in 2 minutes.


You can travel from City 1 to City 3 in 14 minutes, as follows:
 - Use the 1-st railroad to move from City 1 to City 2 in 2 minutes.
 - At the exchange counter in City 2, exchange 3 gold coins for 3 silver coins in 6 minutes.
 - Use the 1-st railroad to move from City 2 to City 1 in 2 minutes.
 - Use the 2-nd railroad to move from City 1 to City 3 in 4 minutes.
"""

def minimum_travel_time(N, M, S, railroads, exchanges):
    from heapq import heappush, heappop
    INF = 1 << 60
    MX_AG = 2500
    
    S = min(S, MX_AG)
    g = [set() for _ in range(N)]
    
    for (u, v, a, b) in railroads:
        u -= 1
        v -= 1
        g[u].add((v, a, b))
        g[v].add((u, a, b))
    
    h = [(0, S, 0)]
    time = [[INF] * (MX_AG + 1) for _ in range(N)]
    time[0][S] = 0
    
    while h:
        (t, ag, loc) = heappop(h)
        for (to, fare, dt) in g[loc]:
            n_Ag = ag - fare
            if n_Ag < 0:
                continue
            cf = time[to][n_Ag]
            n_time = t + dt
            if cf <= n_time:
                continue
            time[to][n_Ag] = n_time
            heappush(h, (n_time, n_Ag, to))
        
        e_time = t + exchanges[loc][1]
        e_Ag = ag + exchanges[loc][0]
        if e_Ag > MX_AG:
            continue
        cf = time[loc][e_Ag]
        if cf <= e_time:
            continue
        time[loc][e_Ag] = e_time
        heappush(h, (e_time, e_Ag, loc))
    
    return [min(time[to]) for to in range(1, N)]
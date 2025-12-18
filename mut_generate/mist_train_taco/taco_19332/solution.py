"""
QUESTION:
Bitville is a seaside city that has a number of shopping centers connected by bidirectional roads, each of which has a travel time associated with it.  Each of the shopping centers may have a fishmonger who sells one or more kinds of fish.  Two cats, Big Cat and Little Cat, are at shopping center $\mbox{1}$ (each of the centers is numbered consecutively from $\mbox{1}$ to $n$).  They have a list of fish they want to purchase, and to save time, they will divide the list between them.  Determine the total travel time for the cats to purchase all of the types of fish, finally meeting at shopping center $n$.  Their paths may intersect, they may backtrack through shopping center $n$, and one may arrive at a different time than the other.  The minimum time to determine is when both have arrived at the destination.  

For example, there are $n=5$ shopping centers selling $k=3$ types of fish.  The following is a graph that shows a possible layout of the shopping centers connected by $m=4$ paths.  Each of the centers is labeled $\textbf{center number/fish types offered/cat(s)}\ \textbf{that visit(s)}$.  Here $\mbox{B}$ and $\boldsymbol{\mbox{L}}$ represent Big Cat and Little Cat, respectively.  In this example, both cats take the same path, i.e. $1\rightarrow3\rightarrow5$ and arrive at time $15+5=20$ having purchased all three types of fish they want.  Neither cat visits shopping centers $2$ or $4$.  

Function Description  

Complete the shop function in the editor below.  It should return an integer that represents the minimum time required for their shopping.  

shop has the following parameters: 

- n: an integer, the number of shopping centers 

- k: an integer, the number of types of fish 

- centers: an array of strings of space-separated integers where the first integer of each element is the number of types of fish sold at a center and the remainder are the types sold 

- roads: a 2-dimensional array of integers where the first two values are the shopping centers connected by the bi-directional road, and the third is the travel time for that road  

Input Format

The first line contains $3$ space-separated integers: $n$ (the number of shopping centers), $m$ (the number of roads), and $\boldsymbol{\mbox{k}}$ (the number of types of fish sold in Bitville), respectively.        

Each line $\boldsymbol{i}$ of the $n$ subsequent lines ($1\leq i\leq n$) describes a shopping center as a line of space-separated integers. Each line takes the following form:

The first integer, $t\left[i\right]$, denotes the number of types of fish that are sold by the fishmonger at the $i^{\mbox{th}}$ shopping center.
Each of the $t\left[i\right]$ subsequent integers on the line describes a type of fish sold by that fishmonger, denoted by $A[i][z]$, where $1\leq z\leq t[i]$ going forward.

Each line $j$ of the $m$ subsequent lines ($1\leq j\leq m$) contains $3$ space-separated integers that describe a road. The first two integers, $u[j]$ and $v[j]$, describe the two shopping centers it connects. The third integer, $w[j]$, denotes the amount of time it takes to travel the road.

Constraints

$2\leq n\leq10^3$
$1\leq m\leq2\times10^3$
$1\leq k\leq10$
$0\leq t[i]\leq k$
$1\leq A[i][z]\leq k$
All $A[i][z]$ are different for every fixed $\boldsymbol{i}$.
$1\leq u[j],v[j]\leq N$
$1\leq w[j]\leq10^4$
Each road connectes $2$ distinct shopping centers (i.e., no road connects a shopping center to itself).
Each pair of shopping centers is directly connected by no more than $\mbox{1}$ road.
It is possible to get to any shopping center from any other shopping center.
Each type of fish is always sold by at least one fishmonger.

Output Format

Print the minimum amount of time it will take for the cats to collectively purchase all $\boldsymbol{\mbox{k}}$ fish and meet up at shopping center $n$.

Sample Input
5 5 5
1 1
1 2
1 3
1 4
1 5
1 2 10
1 3 10
2 4 10
3 5 10
4 5 10

Sample Output
30

Explanation

$\mbox{B}$ represents a location Big Cat visits, $\boldsymbol{\mbox{L}}$ represents a location where Little Cat visits.  

Big Cat can travel $1\to2\to4\to5$ and buy fish at all of the shopping centers on his way.

Little Cat can then travel $1\rightarrow3\rightarrow5$, and buy fish from the fishmonger at the $3^{rd}$ shopping center only.
"""

from heapq import *

def minimum_shopping_time(n, k, centers, roads):
    def get_edges(edgelist, nvert):
        edges = [[] for _ in range(nvert)]
        for (a, b, cost) in edgelist:
            edges[a - 1].append((b - 1, cost))
            edges[b - 1].append((a - 1, cost))
        return edges

    def get_cost(vertexhas, edges, setsize, source):
        costs = [[float('Inf')] * 2 ** setsize for _ in vertexhas]
        heapset = [[] for _ in range(2 ** setsize)]
        heappush(heapset[vertexhas[source]], (0, source))
        for curset, heap in enumerate(heapset):
            while heap:
                cost, vert = heappop(heap)
                oldcost = costs[vert][curset]
                if cost < oldcost:
                    costs[vert][curset] = cost
                    for newvert, newcost in edges[vert]:
                        heappush(heapset[curset | vertexhas[newvert]], (cost + newcost, newvert))
        return costs

    def best_cost(costs):
        costs = list(costs)
        for i in range(len(costs) - 1, -1, -1):
            j = 1
            while j <= i:
                if j & i:
                    costs[i - j] = min(costs[i - j], costs[i])
                j <<= 1
        return min((max(costs[i], costs[~i]) for i in range(len(costs) // 2)))

    # Convert centers to vertexhas
    vertexhas = []
    for center in centers:
        elts = list(map(int, center.split()[1:]))
        vertexhas.append(sum((1 << elt - 1 for elt in elts)))

    # Get edges from roads
    edges = get_edges(roads, n)

    # Calculate costs
    costs = get_cost(vertexhas, edges, k, 0)

    # Return the best cost
    return best_cost(costs[-1])
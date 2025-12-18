"""
QUESTION:
Given a graph which consists of several edges connecting its nodes, find a subgraph of the given graph with the following properties:  

The subgraph contains all the nodes present in the original graph.  
The subgraph is of minimum overall weight (sum of all edges) among all such subgraphs.  
It is also required that there is exactly one, exclusive path between any two nodes of the subgraph. 

One specific node $\mbox{S}$ is fixed as the starting point of finding the subgraph using Prim's Algorithm. 

Find the total weight or the sum of all edges in the subgraph.

Example 

$n=3$ 

$edges=[[1,2,2],[2,3,2],[1,3,3]]$ 

$start=1$   

Starting from node $\mbox{I}$, select the lower weight edge, i.e. $1\leftrightarrow2$, weight $2$.   

Choose between the remaining edges, $1\leftrightarrow3$, weight $3$, and $2\leftrightarrow3$, weight $2$.  

The lower weight edge is $2\leftrightarrow3$ weight $2$.   

All nodes are connected at a cost of $2+2=4$. The edge $1\leftrightarrow3$ is not included in the subgraph.   

Function Description

Complete the prims function in the editor below.  

prims has the following parameter(s):  

int n: the number of nodes in the graph  
int edges[m][3]: each element contains three integers, two nodes numbers that are connected and the weight of that edge  
int start: the number of the starting node  

Returns   

int: the minimum weight to connect all nodes in the graph

Input Format

The first line has two space-separated integers $n$ and $m$, the number of nodes and edges in the graph.  

Each of the next $m$ lines contains three space-separated integers $\mbox{u}$, $\boldsymbol{\nu}$ and $\boldsymbol{w}$, the end nodes of $\textit{edges}[i]$, and the edge's weight. 

The last line has an integer $\textit{start}$, the starting node.  

Constraints

$2\leq n\leq3000$ 

$1\leq m\leq(n*(n-1))/2$ 

$1\le u,v,start\le n$ 

$0\leq w\leq10^5$ 

There may be multiple edges between two nodes.

Sample Input 0
5 6
1 2 3
1 3 4
4 2 6
5 2 2
2 3 5
3 5 7
1

Sample Output 0
15

Explanation 0

The graph given in the test case is shown as :

The starting node is $\mbox{I}$ (in the given test case)

Applying the Prim's algorithm, edge choices available at first are :

$1\rightarrow2$ (WT. 3)  and $1\rightarrow3$ (WT. 4) , out of which $1\rightarrow2$ is chosen (smaller weight of edge).

Now the available choices are : 

$1\rightarrow3$ (WT. 4) , $2\rightarrow3$ (WT. 5) , $2\rightarrow5$ (WT. 2) and $2\rightarrow4$ (WT. 6) , out of which $2\rightarrow5$ is chosen by the algorithm. 

Following the same method of the algorithm, the next chosen edges , sequentially are :

$1\rightarrow3$ and $2\rightarrow4$.

Hence the overall sequence of edges picked up by Prim's are: 

$1\to2:2\to5:1\to3:2\to4$

and the total weight of the MST (minimum spanning tree) is : $3+2+4+6=15$
"""

from collections import defaultdict
import heapq

def prims_minimum_spanning_tree(n, edges, start):
    # Initialize the graph as a defaultdict of sets
    G = defaultdict(set)
    
    # Populate the graph with edges
    for u, v, w in edges:
        G[u].add((w, v))
        G[v].add((w, u))
    
    # Initialize variables for Prim's Algorithm
    E = defaultdict(int)
    D = {}
    T = [0 for _ in range(n + 1)]
    H = [(0, start)]
    
    for node in range(1, n + 1):
        D[node] = float('inf')
    
    D[start] = 0
    
    while H:
        t = heapq.heappop(H)
        for weight, neighbor in G[t[1]]:
            if E[neighbor] == 0 and D[neighbor] > weight:
                D[neighbor] = weight
                if (D[neighbor], neighbor) in H:
                    H.remove((D[neighbor], neighbor))
                    heapq.heapify(H)
                heapq.heappush(H, (D[neighbor], neighbor))
                T[neighbor] = D[neighbor]
            E[t[1]] += 1
    
    # Calculate the total weight of the minimum spanning tree
    total_weight = sum(T[1:])
    return total_weight
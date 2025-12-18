"""
QUESTION:
In a city, N water tanks are connected by pipeline(As a tree) where the ith tank has a capacity cap[i]. The ith element of the given Edge array of length N-1 represents that there is a pipeline between Edge[i][0] and Edge[i][1] tank. Since people working at the city corporation are lazy they usually select one of the tank and pour complete amount of water into it, when the tank is filled, the excess water evenly flows to the connected tanks. The head of city corporation has instructed to pour minimum amount of water into the selected tank so that all other tank is filled. As the labours of the corporation are not intelligent enough to figure out the minimum amount of water required to fill all the tanks they have asked your help. Also Maximum amount of water available with city corporation is 10^{18}.
NOTE: If the tank if full, the water flows to all of its connected tanks except the tank from which the water had come to it. i.e, to all tanks except the source for that particular tank. If it has no option to flow the water is considered to be wasted. S is the source tank.
Example 1:
Input:
N = 4 and S = 1
Edges = [[1, 2], [1, 3], [2, 4]]
Cap = [1, 1, 1, 1]
Output: 5
Explanation:
Initially 5 unit of water is poured into 
tank 1. 2 unit of it flows to tank 2 and 
2 unit of it flows into tank 3. From 2 
unit of water in tank 2, 1 unit flows into 
tank 4 and 1 unit from tank 3 is wasted.
 
Example 2:
Input:
N = 3 and S = 2
Edges = [[1, 2], [2, 3]]
Cap = [1, 1, 1]
Output: 3
Your Task:  
You don't need to read input or print anything. Your task is to complete the function minimum_amount() which takes an integer N, an integer S, 2-d array Edges, and an array Cap of length N as input parameters and returns the minimum amount of water required to fill all the tanks. If it is not possible to fill all the tanks print -1.
Expected Time Complexity: O(N*log(S))
Expected Auxiliary Space: O(1)
 
Constraints:
1 ≤ n ≤ 100000
1 ≤ s,u,v ≤ n
1 ≤ capacity of each tank ≤ 1000000007
"""

def minimum_amount(N, S, Edges, Cap):
    def recur(graph, visited, cur_node, cap):
        if visited[cur_node]:
            return -1
        visited[cur_node] = True
        cur_cap = cap[cur_node - 1]
        max_neigh_cap = 0
        neighbours = 0
        for neigh_node in graph[cur_node]:
            neigh_cap = recur(graph, visited, neigh_node, cap)
            if neigh_cap == -1:
                continue
            max_neigh_cap = max(max_neigh_cap, neigh_cap)
            neighbours += 1
        cur_cap += max_neigh_cap * neighbours
        return cur_cap
    
    graph = {i: [] for i in range(1, N + 1)}
    for (n1, n2) in Edges:
        graph[n1].append(n2)
        graph[n2].append(n1)
    
    visited = [False] * (N + 1)
    res = recur(graph, visited, S, Cap)
    
    for i in range(1, N + 1):
        if not visited[i]:
            return -1
    
    if res > 10 ** 18:
        return -1
    
    return res
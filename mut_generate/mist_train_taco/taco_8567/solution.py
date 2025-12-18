"""
QUESTION:
There are n cities connected by some number of cars. You are given an array of cars where cars[i] =[from_{i},to_{i},cost_{i}] indicates that there is a car from the city from_{i} to city to_{i} with cost price_{i}.
You are also given three integers src,dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
Example 1:
Input:
N=4
cars =  {{ 0,1,100},{1,2,100},{2,0,100},{1,3,600},{2,3,200}}
src = 0
dst = 3
k = 1.
Output:
700
Explanation:
The graph is shown above. The optimal path with at most 1 stops from cities 0 to 3 is marked in red and has cost 100 + 600 = 700. Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
 
Example 2:
Input:
N = 3
cars = {{0,1,100},{1,2,100},{0,2,500}}
src = 0
dst = 2
k = 1
Output:
200
Explanation:
The graph is shown above. The optimal path with at most 1 stops from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function minimumCost() which takes a number of cities N, the cars array cars[], the integer src, the integer dst, and the number of stops k as input parameters and returns the minimum cost else -1.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{2}
0<= edges[i][0],edges[i][1] 1<=edges[i][2]<=10^{4}
0<=src,dst,k src!=dst
"""

from typing import List

def find_cheapest_price(n: int, cars: List[List[int]], src: int, dst: int, k: int) -> int:
    # Create a dictionary to represent the graph
    graph = {i: [] for i in range(n)}
    for from_i, to_i, cost_i in cars:
        graph[from_i].append((to_i, cost_i))
    
    # Initialize the cost array with a large number
    costs = [float('inf')] * n
    costs[src] = 0
    
    # Initialize the queue with the source city, cost, and stop count
    queue = [(src, 0, 0)]
    
    # Process the queue
    while queue:
        pos, wt, cnt = queue.pop(0)
        for to_i, cost_i in graph[pos]:
            if wt + cost_i < costs[to_i] and cnt <= k:
                costs[to_i] = wt + cost_i
                queue.append((to_i, wt + cost_i, cnt + 1))
    
    # If the destination cost is still infinity, return -1
    return costs[dst] if costs[dst] != float('inf') else -1
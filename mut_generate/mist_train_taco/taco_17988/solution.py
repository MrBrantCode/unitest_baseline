"""
QUESTION:
As White Walkers have attacked Winterfell, Cersei has to send her army to Winterfell but through tunnels.
Unwilling to do so, she wants to delay as much as she can so she take the longest route to Winterfell.
You are given no of tunnels(n) followed by tunnel 'u' connecting tunnel 'v' having distance 'w'. 
Now, you being a fan of Cersei, is keen to find the longest route.
Example 1:
Ã¢â¬â¹Input : 
arr[ ] = {{1, 5, 3}, {3, 5, 5}, {5, 4, 2}, 
{2, 4, 5}, {4, 7, 6}, {7, 8, 2}, {7, 6, 1}} 
and N = 8
Output : 14
Explanation:
If we consider the path between 8 and 3 then 
it add up to the sum equal to 14.
Example 2:
Input : arr[ ] = {{1, 2, 3},{2, 3, 1}} and 
N = 3 
Output :  4
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function longest_route() that takes a 2-d array (arr), number of tunnels (N), and return the length of the longest route. The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ N ≤ 7000
1 ≤ u,v ≤ N
1 ≤ w ≤ 500
"""

def find_longest_route(arr, n):
    # Create adjacency list
    adj = [[] for _ in range(n)]
    for u, v, w in arr:
        adj[u - 1].append((v - 1, w))
        adj[v - 1].append((u - 1, w))
    
    # Initialize distance array
    dist = [-1] * n
    dist[0] = 0
    
    # Perform DFS from the first node
    dfs(adj, 0, dist)
    
    # Find the farthest node from the first node
    idx = max(enumerate(dist), key=lambda x: x[1])[0]
    
    # Reinitialize distance array
    dist = [-1] * n
    dist[idx] = 0
    
    # Perform DFS from the farthest node
    dfs(adj, idx, dist)
    
    # The longest route is the maximum distance found
    return max(dist)

def dfs(adj, v, dist):
    for (w, d) in adj[v]:
        if dist[w] == -1:
            dist[w] = dist[v] + d
            dfs(adj, w, dist)
"""
QUESTION:
Barney lives in country USC (United States of Charzeh). USC has n cities numbered from 1 through n and n - 1 roads between them. Cities and roads of USC form a rooted tree (Barney's not sure why it is rooted). Root of the tree is the city number 1. Thus if one will start his journey from city 1, he can visit any city he wants by following roads.

<image>

Some girl has stolen Barney's heart, and Barney wants to find her. He starts looking for in the root of the tree and (since he is Barney Stinson not a random guy), he uses a random DFS to search in the cities. A pseudo code of this algorithm is as follows:
    
    
      
    let starting_time be an array of length n  
    current_time = 0  
    dfs(v):  
    	current_time = current_time + 1  
    	starting_time[v] = current_time  
    	shuffle children[v] randomly (each permutation with equal possibility)  
    	// children[v] is vector of children cities of city v  
    	for u in children[v]:  
    		dfs(u)  
    

As told before, Barney will start his journey in the root of the tree (equivalent to call dfs(1)).

Now Barney needs to pack a backpack and so he wants to know more about his upcoming journey: for every city i, Barney wants to know the expected value of starting_time[i]. He's a friend of Jon Snow and knows nothing, that's why he asked for your help.

Input

The first line of input contains a single integer n (1 ≤ n ≤ 105) — the number of cities in USC.

The second line contains n - 1 integers p2, p3, ..., pn (1 ≤ pi < i), where pi is the number of the parent city of city number i in the tree, meaning there is a road between cities numbered pi and i in USC.

Output

In the first and only line of output print n numbers, where i-th number is the expected value of starting_time[i].

Your answer for each city will be considered correct if its absolute or relative error does not exceed 10 - 6.

Examples

Input

7
1 2 1 1 4 4


Output

1.0 4.0 5.0 3.5 4.5 5.0 5.0 


Input

12
1 1 2 2 4 4 3 3 1 10 8


Output

1.0 5.0 5.5 6.5 7.5 8.0 8.0 7.0 7.5 6.5 7.5 8.0
"""

def calculate_expected_starting_times(n, parents):
    # Initialize the parent array with -1 for city 1 and adjust the rest
    par = [-1] + [p - 1 for p in parents]
    
    # Initialize the children list
    child = [[] for _ in range(n)]
    for i in range(1, n):
        child[par[i]].append(i)
    
    # Initialize the size array
    size = [1] * n
    
    # First DFS to calculate the size of each subtree
    def dfs():
        stack = [0]
        visit = [False] * n
        while stack:
            u = stack[-1]
            if not visit[u]:
                for v in child[u]:
                    stack.append(v)
                visit[u] = True
            else:
                for v in child[u]:
                    size[u] += size[v]
                stack.pop()
    
    # Initialize the answer array
    ans = [0] * n
    ans[0] = 1
    
    # Second DFS to calculate the expected starting times
    def dfs2():
        stack = [0]
        while stack:
            u = stack.pop()
            sm = 0
            for v in child[u]:
                sm += size[v]
            for v in child[u]:
                ans[v] = (sm - size[v]) * 0.5 + 1 + ans[u]
                stack.append(v)
    
    # Perform the DFSs
    dfs()
    dfs2()
    
    # Return the expected starting times
    return ans
"""
QUESTION:
The country of Byteland contains $N$ cities and $N-1$ bidirectional roads. There is a path between any two cities. The roads in Byteland were built long ago, and now they are in need of repair. You have been hired to fix all the roads. You intend to do this by dispatching robots on some of the roads. Each robot will repair the road he is currently on and then moves to one of the adjacent unrepaired roads. After repairing that, it will move to another adjacent unrepaired road, repair that and so on.

Two roads are adjacent if they have the same city at one of their endpoints. For the process to be efficient, no two robots will ever repair the same road, and no road can be visited twice. What is the minimum number of robots needed to accomplish the task?

Input Format

The first line contains the number of test cases $\mathbf{T}$. $\mathbf{T}$ test cases follow. The first line of each test case contains $N$, the number of cities in Byteland. The cities are numbered $\textbf{0.N-1}$. The following $N-1$ lines contain the description of the roads. The $i^{\mbox{th}}$ line contains two integers $a_i$ and $b_i$, meaning that there is a road connecting cities with numbers $a_i$ and $b_i$.

Constraints

$1\leq T\leq20$  
$1\leq N\leq10000$  
$0\leq a_i,b_i<N$

Output Format

Print $\mathbf{T}$ lines, one corresponding to each test case containing the required answer for that test case.

Sample Input
3  
4  
0 1  
0 2  
0 3  
6  
0 1  
1 2  
2 3  
2 4  
4 5  
7  
0 1  
1 2  
2 3  
2 4  
4 5  
3 6

Sample Output
1  
1  
2

Explanation

For the first case, one robot is enough to repair all roads: $(0,1)\rightarrow(0,2)\rightarrow(0,3)$ 

For the second case, one robot is again enough: $(0,1)\to(1,2)\to(2,3)\to(2,4)\to(4,5)$ 

The the third case, there is no way to repair all the roads with one robot and at least two are needed.
"""

import collections
import queue

def minimum_robots_needed(n, roads):
    # Create the graph
    graph = collections.defaultdict(list)
    for (x, y) in roads:
        graph[x].append(y)
        graph[y].append(x)
    
    # BFS initialization
    level = 1
    root = 0
    q = queue.Queue()
    q.put((root, level, None))
    seen = set()
    levels = collections.defaultdict(set)
    tree = {}
    
    # BFS traversal
    while not q.empty():
        item, level, parent = q.get()
        levels[level].add(item)
        seen.add(item)
        tree[item] = dict(id=item, parent=parent, level=level, children=set(), leaf=None)
        for child in graph[item]:
            if child not in seen:
                q.put((child, level + 1, item))
                seen.add(child)
                tree[item]['children'].add(child)
    
    # Calculate the minimum number of robots needed
    clusters = 1
    has_items_in_cluster = False
    for level in sorted(levels.keys(), reverse=True):
        for item in levels[level]:
            tree_item = tree[item]
            if not tree_item['children']:
                tree_item['leaf'] = True
            else:
                has_items_in_cluster = True
                branches = 0
                for child in tree_item['children']:
                    if not tree[child]['leaf']:
                        branches += 1
                if branches >= 2:
                    new_clusters = branches // 2
                    clusters += new_clusters
                    if branches % 2 == 0:
                        has_items_in_cluster = False
                        parent = tree_item['parent']
                        if parent is not None:
                            tree[parent]['children'].remove(item)
    
    if not has_items_in_cluster:
        clusters -= 1
    
    return clusters
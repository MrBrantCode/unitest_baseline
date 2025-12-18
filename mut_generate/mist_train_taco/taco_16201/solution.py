"""
QUESTION:
Zombies have placed themselves at every junction in Bucharest. Each junction 'i' initially has a presence of ai number of zombies. Every timestep, each zombie randomly chooses one of its neighboring junctions and walks towards it. Each neighboring junction is choosen by the zombie with an equal probability. In order to safegaurd the citizens of Bucharest we need to find out the expected number of zombies at every junction after 'k' timesteps. 

The network of Bucharest is given as an edge list.  

Input Format  

t - the number of test cases. 't' cases follow.
n, m, k - 'n' junctions (nodes) in Bucharest, 'm' roads (edges) and 'k' time steps. 
This is followed by m lines containing 1 edge on each line. Each edge is denoted by 2 integers representing the nodes it connects, which can range from 0 to n-1.  All the edges are bidirectional. A node cannot connect itself. 
This is followed by n lines, where the i^{th} line contains the initial number of Zombies at the location ai.

Output Format 

Output the number of zombies (rounded of to its nearest integer) in the 5 most highly populated junctions after 'k' timesteps.

Constraints 

1<=t<=5

5<=n<=100000

1<=m<= 200000

1<=k<=10000000

1<=ai<=1000

Sample Input  

1

10 18 100

0 8 

0 5 

1 2 

1 5 

2 8 

2 4 

2 5 

2 6 

3 5 

4 8 

4 6 

4 7 

5 8 

5 9 

6 8 

6 9 

7 9 

8 9 

1

1

1

1

1

1

1

1

1

1

Sample Output 

2 2 1 1 1
"""

def simulate_zombie_population(num_nodes, edges, initial_zombie_counts, time_steps):
    # Create a list to store the neighbors of each node
    neighbors_by_node = [[] for _ in range(num_nodes)]
    
    # Populate the neighbors list based on the edges
    for node1, node2 in edges:
        neighbors_by_node[node1].append(node2)
        neighbors_by_node[node2].append(node1)
    
    # Function to compute the expected number of zombies at each node after one timestep
    def compute_incoming_zombies(node):
        return sum([initial_zombie_counts[neighbor] / len(neighbors_by_node[neighbor]) for neighbor in neighbors_by_node[node]])
    
    # Initialize the zombie counts with the initial values
    zombie_count_by_node = initial_zombie_counts[:]
    
    # Simulate the zombie movement for the given number of time steps
    for _ in range(time_steps):
        new_zombie_counts_by_node = [compute_incoming_zombies(node) for node in range(num_nodes)]
        zombie_count_by_node = new_zombie_counts_by_node
    
    # Sort the zombie counts in descending order and take the top 5
    top_5_zombie_counts = sorted(zombie_count_by_node, reverse=True)[:5]
    
    # Round the zombie counts to the nearest integer
    rounded_top_5_zombie_counts = [round(count) for count in top_5_zombie_counts]
    
    return rounded_top_5_zombie_counts
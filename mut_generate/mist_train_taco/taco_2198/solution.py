"""
QUESTION:
Under the command "Save Sergeant Ryan," Aiz's rescue team fought fierce battles with enemy forces in the floating city of Lee, Germany. They successfully joined the sergeant, but there were many enemy tanks and they could not call a rescue herio. So, in order to confuse the enemy tanks, they decided to carry out an operation to blow up all the bridges in the city.

The operation was immediately communicated to HQ and preparations for a rescue helicopter were underway. In order to fly the rescue herio, you have to predict when all the bridges will be blown up. As a military programmer, your mission is to calculate the time the rescue team will need to blow up all the bridges.

The floating city is made up of N islands, with a bridge between the islands. All the islands are connected in a tree shape (see the figure below). There is only one route from one island to another. It takes a fixed amount of time to cross each bridge, and it is possible to cross the bridge in either direction at that time.

Rescue units do not have the means to move on the water, such as boats, so the only way to move between islands is through a bridge. Rescue units can instantly blow up the bridges adjacent to the island at that time. What is the minimum time required for a rescue unit to blow up all the bridges? However, we do not consider the travel time within the island.

Create a program that inputs the number of islands and information on each bridge and outputs the minimum time required to blow up all the bridges. Each island is represented by a number from 1 to N. There are N-1 bridges. The bridge information consists of the numbers (a, b) of the two islands adjacent to the bridge and the time t required to cross the bridge. Rescue units shall start on the island with island number 1.

<image>



Input

A sequence of multiple datasets is given as input. The end of the input is indicated by a single line of zeros. Each dataset is given in the following format.


N
a1 b1 t1
a2 b2 t2
::
aN-1 bN-1 tN-1


All inputs are given as integers. The number of islands N (2 ≤ N ≤ 20) is given on the first line.

The following N-1 line gives information on the i-th bridge. ai, bi, ti (1 ≤ ti ≤ 500) means that we can move between island ai and island bi in time ti through the i-th bridge.

The number of datasets does not exceed 100.

Output

For each dataset, print the minimum time required to blow up all the bridges on one line.

Example

Input

7
1 2 5
2 3 2
3 4 3
2 5 3
5 6 3
5 7 8
0


Output

12
"""

def calculate_minimum_time(N, bridges):
    # Initialize the adjacency matrix
    R = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    
    # Fill the adjacency matrix with bridge times
    total = 0
    for a, b, t in bridges:
        R[a][b] = t
        R[b][a] = t
        total += t * 2
    
    # Depth-first search to find the maximum path length
    def dfs_max(cur, pre):
        _max = -R[cur][pre]
        for i in range(N + 1):
            if R[cur][i] > 0 and i != pre:
                _max = max(_max, dfs_max(i, cur) + R[cur][i])
        return _max
    
    # Adjust total time based on single-bridge islands
    for i in range(2, N + 1):
        spam = [x for x in R[i] if x > 0]
        if len(spam) <= 1:
            total -= spam[0] * 2
    
    # Calculate and return the minimum time required
    return total - dfs_max(1, 0)
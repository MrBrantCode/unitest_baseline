"""
QUESTION:
Squirrel Liss loves nuts. There are n trees (numbered 1 to n from west to east) along a street and there is a delicious nut on the top of each tree. The height of the tree i is h_{i}. Liss wants to eat all nuts.

Now Liss is on the root of the tree with the number 1. In one second Liss can perform one of the following actions:  Walk up or down one unit on a tree.  Eat a nut on the top of the current tree.  Jump to the next tree. In this action the height of Liss doesn't change. More formally, when Liss is at height h of the tree i (1 ≤ i ≤ n - 1), she jumps to height h of the tree i + 1. This action can't be performed if h > h_{i} + 1. 

Compute the minimal time (in seconds) required to eat all nuts.


-----Input-----

The first line contains an integer n (1  ≤  n ≤ 10^5) — the number of trees.

Next n lines contains the height of trees: i-th line contains an integer h_{i} (1 ≤ h_{i} ≤ 10^4) — the height of the tree with the number i.


-----Output-----

Print a single integer — the minimal time required to eat all nuts in seconds.


-----Examples-----
Input
2
1
2

Output
5

Input
5
2
1
2
1
1

Output
14
"""

def calculate_minimal_time_to_eat_nuts(n, heights):
    # Initialize the total time and the current height
    total_time = n
    current_height = 0
    
    # Calculate the time to reach and eat the nut on the first tree
    total_time += heights[0] - current_height
    current_height = heights[0]
    
    # Iterate through the rest of the trees
    for i in range(1, n):
        if current_height <= heights[i]:
            total_time += 1 + heights[i] - current_height
            current_height = heights[i]
        else:
            total_time += 1 + current_height - heights[i]
            current_height = heights[i]
    
    return total_time
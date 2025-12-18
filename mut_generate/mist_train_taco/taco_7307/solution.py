"""
QUESTION:
Given is an integer sequence of length N+1: A_0, A_1, A_2, \ldots, A_N. Is there a binary tree of depth N such that, for each d = 0, 1, \ldots, N, there are exactly A_d leaves at depth d? If such a tree exists, print the maximum possible number of vertices in such a tree; otherwise, print -1.

Constraints

* 0 \leq N \leq 10^5
* 0 \leq A_i \leq 10^{8} (0 \leq i \leq N)
* A_N \geq 1
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N
A_0 A_1 A_2 \cdots A_N


Output

Print the answer as an integer.

Examples

Input

3
0 1 1 2


Output

7


Input

4
0 0 1 0 2


Output

10


Input

2
0 3 1


Output

-1


Input

1
1 1


Output

-1


Input

10
0 0 1 1 2 3 5 8 13 21 34


Output

264
"""

def calculate_max_vertices(n, a):
    # Calculate the cumulative sum of the sequence from the end to the beginning
    cumsum_a = a.copy()
    for i in range(n - 1, -1, -1):
        cumsum_a[i] += cumsum_a[i + 1]
    
    # Initialize the answer and the number of nodes at the current depth
    ans = 0
    node = 1
    
    # Iterate through each depth level
    for i in range(n + 1):
        # If the number of leaves at the current depth exceeds the available nodes, return -1
        if a[i] > node:
            return -1
        
        # Add the number of nodes at the current depth to the answer
        ans += node
        
        # Calculate the number of nodes available for the next depth level
        if i < n:
            node = min(2 * (node - a[i]), cumsum_a[i + 1])
    
    return ans
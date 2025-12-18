"""
QUESTION:
In the game of Restricted Pacman, an infinite linear path is given. Pacman has to start at position 0 and eat as many candies as possible. In one move he can only jump a distance of either M or N.  If M and N are coprime numbers, find how many candies will be left on the board after the game is over.
Note: The result is always finite as after a point X every index in the infinite path can be visited. 
Example 1:
Input: M = 2, N = 5
Output: 2
Explanation: From index 0, the indices that 
can be visited are
0 + 2 = 2
0 + 2 + 2 = 4
0 + 5 = 5
0 + 2 + 2 + 2 = 6
0 + 2 + 5 = 7
0 + 2 + 2 + 2 + 2 = 8
0 + 2 + 2 + 5 = 9
0 + 5 + 5 = 10
and so on.
1 and 3 are the only indices that cannot be 
visited. Therefore the candies at these two 
positions will be left on the board. 
Example 2:
Input: M = 2, N = 7
Output: 3 
Example 3:
Input: M = 25, N = 7
Output: 72
Your Task:  
You don't need to read input or print anything. Complete the function candies() which take M and N as input parameters and return the answer.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 < M, N ≤ 500
"""

import math
from collections import deque

def count_remaining_candies(m: int, n: int) -> int:
    # Calculate the least common multiple (LCM) of m and n
    ma = m * n // math.gcd(m, n)
    
    # Initialize a list to mark visited positions
    marked = [0] * ma
    marked[0] = 1  # Starting position is visited
    
    # Initialize a queue for BFS
    q = deque()
    q.append(0)
    
    # Perform BFS to mark all reachable positions
    while q:
        curr = q.popleft()
        if curr + m < ma and marked[curr + m] == 0:
            marked[curr + m] = 1
            q.append(curr + m)
        if curr + n < ma and marked[curr + n] == 0:
            marked[curr + n] = 1
            q.append(curr + n)
    
    # Count and return the number of unvisited positions
    return marked.count(0)
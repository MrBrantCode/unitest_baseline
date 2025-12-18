"""
QUESTION:
Given a 5x6 snakes and ladders board, find the minimum number of dice throws required to reach the destination or last cell (30^{th} cell) from the source (1st cell). 
You are given an integer N denoting the total number of snakes and ladders and an array arr[] of 2*N size where 2*i and (2*i + 1)^{th} values denote the starting and ending point respectively of i^{th }snake or ladder. The board looks like the following.
Note: Assume that you have complete control over the 6 sided dice. No ladder starts from 1st cell.
                                   
Example 1:
Input:
N = 8
arr[] = {3, 22, 5, 8, 11, 26, 20, 29, 
       17, 4, 19, 7, 27, 1, 21, 9}
Output: 3
Explanation:
The given board is the board shown
in the figure. For the above board 
output will be 3. 
a) For 1st throw get a 2. 
b) For 2nd throw get a 6.
c) For 3rd throw get a 2.
Your Task:
You do not need to read input or print anything. Your task is to complete the function minThrow() which takes N and arr as input parameters and returns the minimum number of throws required to reach the end of the game.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10
1 ≤ arr[i] ≤ 30
"""

from collections import deque

def min_throws_to_reach_end(N, arr):
    snakes_ladders = {}
    for i in range(0, 2 * N, 2):
        snakes_ladders[arr[i]] = arr[i + 1]
    
    q = deque([(1, 0)])  # (current_position, number_of_throws)
    visited = set([1])
    
    while q:
        curr_pos, num_throws = q.popleft()
        if curr_pos == 30:
            return num_throws
        
        for i in range(1, 7):
            next_pos = curr_pos + i
            if next_pos > 30:
                continue
            if next_pos in snakes_ladders:
                next_pos = snakes_ladders[next_pos]
            if next_pos not in visited:
                visited.add(next_pos)
                q.append((next_pos, num_throws + 1))
    
    return -1
"""
QUESTION:
You are given an infinite two-dimensional grid. There are N balloons placed at certain coordinates of the grid. You have an arrow with yourself, which you will be using to shoot the balloons. You can select any point on the grid as your starting point and any point on the grid as the target point. When you fire the arrow, all ballons lying on the shortest path between the starting point and target point will be burst. Given the coordinates of the N ballons in an array arr, your task is to find out the maximum number of balloons that you can fire in one arrow shot.
Example 1:
Input:
N = 3
arr[] = {{1, 2}, {2, 3}, {3, 4}}
Output:
3
Explanation:
If you position yourself at point (1,2)
and fire the arrow aiming at the point (3,4).
Then all the balloons will burst.
Example 2:
Input: 
N = 3
arr[] = {{2,2}, {0,0}, {1,2}} 
Output:
2
Explanation: 
If you position yourself at point (2,2)
and fire the arrow aiming at the point (0,0).
Then the two balloons present at the two points
will burst.
Your Task:
Complete the function mostBalloons() which takes the integers N and the array arr as the input parameters, and returns the maximum number of balloons that can be burst using one arrow.
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{3}
-10^{9} ≤ arr[i][j] ≤ 10^{9}
"""

from math import gcd

def max_balloons_burst(N, arr):
    if N < 3:
        return N
    
    ans = 0
    
    for i in range(N - 1):
        a = arr[i]
        di = {}
        curr = 1
        
        for j in range(i + 1, N):
            b = arr[j]
            rise = b[1] - a[1]
            run = b[0] - a[0]
            
            if rise == 0 and run == 0:
                curr += 1
            elif rise == 0 or run == 0:
                if rise:
                    s = 10 ** 9 + 1
                else:
                    s = 0
                di[s] = di.get(s, 0) + 1
            else:
                s = rise / run
                di[s] = di.get(s, 0) + 1
        
        for count in di.values():
            ans = max(ans, count + curr)
    
    return ans
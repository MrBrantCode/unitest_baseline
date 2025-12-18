"""
QUESTION:
A car factory has two assembly lines, and also given an  2D array a[2][] of size N which represent the time taken by each station. Each station is dedicated to some sort of work like engine fitting, body fitting, painting, and so on. So, a car chassis must pass through each of the n stations in order before exiting the factory. The two parallel assemble line perform same task.
From any line one can switch another line diagonally. A 2D array T[2][] of size N is also given, which represent  exit time to switch line 1 to line 2 diagonally.
Also each assembly line takes an entry time e_{i} and exit time x_{i} which may be different for the two lines.
For more clarity, refer the following diagram
The task is to computing the minimum time it will take to build a car chassis.
One can minimize the total time taken by performing following steps:
	 A car chassis must pass through all stations from 1 to N in order(in any of the two assembly lines). i.e. it cannot jump from station i to station j if they are not at one move distance.
	The car chassis can move one station forward in the same line, or one station diagonally in the other line. It incurs an extra cost T_{i,j} to move to station j from line i. No cost is incurred for movement in same line.
	The time taken in station j on line i is a_{i, j}.
Example 1:
Input: N = 4
a[2][] = {{4, 5, 3, 2}, 
      {2, 10, 1, 4}}
T[2][] = {{0,7, 4, 5},
           {0,9, 2, 8}}
e[2] = {10,12}, x[2] = {18,7}
Output: 35
Explanation: 
According to the TC, this would 
be the following diagram
The bold line shows the path covered by the 
car chassis for given input values. So the minimum 
time taken by the car is 35.
Your Task:
You don't need to read input or print anything. Your task is to complete the function carAssembly() which takes two array of integers a,T of size n and array of e and x of size 2 as parameters and returns an integer denoting the answer.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ a[2][], T[2][], e[], x[] ≤ 10^{6}
"""

from typing import List

def carAssembly(n: int, a: List[List[int]], T: List[List[int]], e: List[int], x: List[int]) -> int:
    # Add exit times to the last station of each line
    a[0][-1] += x[0]
    a[1][-1] += x[1]
    
    # Add entry times to the first station of each line
    a[0][0] += e[0]
    a[1][0] += e[1]
    
    # Compute the minimum time for each station from the end to the start
    for i in range(n - 2, -1, -1):
        a[0][i] = a[0][i] + min(a[0][i + 1], T[0][i + 1] + a[1][i + 1])
        a[1][i] = a[1][i] + min(a[1][i + 1], T[1][i + 1] + a[0][i + 1])
    
    # Return the minimum time to exit from either line
    return min(a[0][0], a[1][0])
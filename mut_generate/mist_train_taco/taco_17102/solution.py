"""
QUESTION:
Given the co-effecients of X,Y and Z in a system of simultaneous equations. Find the values of X,Y and Z.
 a1X + b1Y + c1Z = d1
 a2X + b2Y + c2Z = d2
 a3X + b3Y + c3Z = d3
Example 1:
Input: 
Arr = {{5, 4, 2, 0},
       {1, 4, 2, 0},
       {4, 2, 9, 0}}
Output: {0, 0, 0} 
Explanation: After calculating with these
given coefficient the value of X, Y, Z is
0, 0, 0.
Example 2:
Input: 
Arr = {{4.2, 6, 7, 10},
       {1, 2, 3, 12},
       {3, 2, 2, 20}}
Output: {3, 4, -1}
Explanation: After calculating with these
given coefficient the value of X, Y, Z is
3, 4, -1. 
Your Task:  
You dont need to read input or print anything. Complete the function myCalculator() which takes Arr as input parameter and returns 0 in case the system is inconsistent and 1 in case the system is consistent and has infinitely many solutions. In case the system is consistent and has a unique solution, return 3 space separated integers denoting the floor values of X, Y and Z respectively.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
-100 <= Arr[i][j] <=100
"""

import math

def delta(Arr, i, j, k):
    ans = Arr[0][i] * Arr[1][j] * Arr[2][k]
    ans += Arr[0][j] * Arr[1][k] * Arr[2][i]
    ans += Arr[0][k] * Arr[1][i] * Arr[2][j]
    ans -= Arr[0][i] * Arr[1][k] * Arr[2][j]
    ans -= Arr[0][j] * Arr[1][i] * Arr[2][k]
    ans -= Arr[0][k] * Arr[1][j] * Arr[2][i]
    return ans

def solve_simultaneous_equations(Arr):
    d = delta(Arr, 0, 1, 2)
    p = delta(Arr, 3, 1, 2)
    q = delta(Arr, 0, 3, 2)
    r = delta(Arr, 0, 1, 3)
    
    if d == 0:
        if p == 0 and q == 0 and r == 0:
            return 1
        else:
            return 0
    
    return [int(p // d), int(q // d), int(r // d)]
"""
QUESTION:
A city of dimension N x N is constructed with grid of lanes. These lanes are fenced by government so that no one can cross any grid diagonally. Although a train 
line runs diagonally from (0,0) to (N,N).
Our chef has a weird kind of phobia and is very afraid to cross the railway line. He is at point (0,0) and wants to get to the point (N,N). Calculate number of path 
through which it is possible to reach to its destination travelling the minimum distance. .
Note that: 

1. Since he is already at position (0,0) he can go to either part of grid (i.e. left or right part - divided by diagonal) but he will remain in that part for the whole path.
2. He is only afraid to "cross" the line, i.e. during the route he can go to position (m,m) where 0
3. You have to calculate the number of path possible. If there is more than one path then you have to print the number of path of minimum distances. 

-----Input-----
The first line of the input contains an integer T denoting the number of test cases, for each test case enter the grid size i.e value of N.

-----Output-----
For each test case, output a single line with number of such paths possible.
(Note : If no such path possible print 0)

-----Constraints-----
- 1 <= T <= 100
- 0 <= N <= 30

-----Example-----
Input:
2
2
5
Output:
4
84
"""

def calculate_minimum_paths(N: int) -> int:
    if N == 0:
        return 0
    
    # Precompute Catalan numbers up to 30
    catalan_numbers = [0] * 31
    catalan_numbers[0] = 1
    
    for i in range(1, 31):
        catalan_numbers[i] = catalan_numbers[i - 1] * (4 * i - 2) // (i + 1)
    
    # The number of paths is 2 times the Catalan number of N
    return catalan_numbers[N] * 2
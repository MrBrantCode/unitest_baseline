"""
QUESTION:
How many ways are there to place a black and a white knight on an N * M chessboard such that they do not attack each other? The knights have to be placed on different squares. A knight can move two squares horizontally and one square vertically, or two squares vertically and one square horizontally. The knights attack each other if one can reach the other in one move.

------ Input : ------ 

The first line contains the number of test cases T. Each of the next T lines contains two integers N and M.

------ Output : ------ 

Output T lines, one for each test case, each containing the required answer for the corresponding test case.

------ Constraints : ------ 

1 ≤ T ≤ 10000
1 ≤ N,M ≤ 100000

----- Sample Input 1 ------ 
3
2 2
2 3
4 5
----- Sample Output 1 ------ 
12
26
312
"""

def count_knight_placements(n, m):
    ans = 0
    if n > 2 and m > 1:
        ans += (n - 2) * (m - 1) * 2
    if m > 2 and n > 1:
        ans += (m - 2) * (n - 1) * 2
    ans = n * m * (n * m - 1) - 2 * ans
    return ans
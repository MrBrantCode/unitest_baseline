"""
QUESTION:
Devu loves to play with his dear mouse Jerry.  One day they play a game on 2 dimensional grid of dimensions n * n (n ≥ 2). Jerry is currently at coordinates (sx, sy) and wants to move to location (ex, ey) where cheese is placed by Devu. Also Devu is very cunning and has placed a bomb at location (bx, by). All these three locations are distinct. 

In a single move, Jerry can go either up, down, left or right in the grid such that it never goes out of the grid. Also, it has to avoid the bomb. Find out minimum number of moves Jerry needs. It is guaranteed that it is always possible to do so.

-----Input-----
- The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows."
- The first line of each test case contains seven space separated integers n, sx, sy , ex, ey, bx, by. 

-----Output-----
- For each test case, output a single line containing an integer corresponding to minimum number of moves Jerry needs.

-----Constraints-----
- 1 ≤ T ≤ 1000
- 2 ≤ n ≤ 20
-  1 ≤ sx, sy , ex, ey, bx, by ≤ n 
- No two or more poitns in the three points are same.

-----Example-----
Input:
2
2 1 1 2 2 1 2
3 1 1 1 3 1 2

Output:
2
4

-----Explanation-----
Example case 1. ...
Jerry will move directly (1, 1) to (2, 1) and then to (2, 2) in total 2 moves.

Example case 2. ...
"""

def calculate_minimum_moves(n, sx, sy, ex, ey, bx, by):
    # If Jerry moves in both x and y directions
    if sx != ex and sy != ey:
        return abs(sx - ex) + abs(sy - ey)
    
    # If Jerry moves only in the x direction
    elif sx == ex:
        if sx == bx:
            if (by > sy and by < ey) or (by < sy and by > ey):
                return abs(sx - ex) + abs(sy - ey) + 2
            else:
                return abs(sx - ex) + abs(sy - ey)
        else:
            return abs(sx - ex) + abs(sy - ey)
    
    # If Jerry moves only in the y direction
    elif sy == ey:
        if sy == by:
            if (bx > sx and bx < ex) or (bx < sx and bx > ex):
                return abs(sx - ex) + abs(sy - ey) + 2
            else:
                return abs(sx - ex) + abs(sy - ey)
        else:
            return abs(sx - ex) + abs(sy - ey)
    
    # Default case (should not be reached due to problem constraints)
    else:
        return abs(sx - ex) + abs(sy - ey)
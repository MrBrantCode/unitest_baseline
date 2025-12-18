"""
QUESTION:
There is a knight - the chess piece - at the origin (0, 0) of a two-dimensional grid.
When the knight is at the square (i, j), it can be moved to either (i+1,j+2) or (i+2, j+1).
In how many ways can the knight reach the square (X, Y)?
Find the number of ways modulo 10^9 + 7.

-----Constraints-----
 - 1 \leq X \leq 10^6
 - 1 \leq Y \leq 10^6
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
X Y

-----Output-----
Print the number of ways for the knight to reach (X, Y) from (0, 0), modulo 10^9 + 7.

-----Sample Input-----
3 3

-----Sample Output-----
2

There are two ways: (0,0) \to (1,2) \to (3,3) and (0,0) \to (2,1) \to (3,3).
"""

def count_knight_moves(X: int, Y: int) -> int:
    MOD = 10**9 + 7
    
    # Calculate c1
    c1 = 2 * Y - X
    if c1 % 3 != 0:
        return 0
    c1 //= 3
    
    # Check if the moves are feasible
    if c1 < 0 or X - c1 < 0 or Y - 2 * c1 < 0:
        return 0
    
    # Calculate c2
    c2 = Y - 2 * c1
    
    # Calculate the number of combinations
    c3 = c1 + c2 + 1
    c4 = min(c1, c2)
    
    # Calculate the binomial coefficient (c3 choose c4) % MOD
    x = 1
    y = 1
    for i in range(1, c4 + 1):
        x = x * (c3 - i) % MOD
        y = y * i % MOD
    
    result = x * pow(y, MOD - 2, MOD) % MOD
    return result
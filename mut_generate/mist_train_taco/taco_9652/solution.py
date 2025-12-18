"""
QUESTION:
------ Problem Statement ------ 

Past

In the year of 2048, the Virtual Reality Massively Multiplayer Online Role-Playing Game (VRMMORPG), Code Art Online (CAO), is released. With the Chef Gear, a virtual reality helmet that stimulates the user's five senses via their brain, players can experience and control their in-game characters with their minds.

On August the 2nd, 2048, all the players log in for the first time, and subsequently discover that they are unable to log out. They are then informed by Code Master, the creator of CAO, that if they wish to be free, they must reach the second stage of the game.

Kirito is a known star player of CAO. You have to help him log out.

Present

Stage 1

A map is described by a 2D grid of cells. Each cell is either labelled as a # or a ^. # denotes a wall. A monster exists in a cell if the cell is not a wall and the cell is a centre of Prime-Cross (CPC).
Let L be the number of contiguous ^ to the left of X, in the same row as X.
R be the number of contiguous ^ to the right of X, in the same row as X.
T be the number of contiguous ^ above X, in the same column as X.
B be the number of contiguous ^ below X, in the same column as X.

A cell X is said to be a CPC if there exists a prime number P such that P ≤ minimum of [L, R, T, B].

Note: While computing L, R, T, B for a cell X, you should not count the ^ of the cell X.

Given a map, you have to tell Kirito the number of cells where monsters exist.

Future

If you are done with this task, go help Kirito with Stage 2 :-)

------ Input ------ 

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows. Each case starts with a line containing two space separated integers R, C denoting the number of rows and columns in the map respectively. The next R lines contain C characters each, describing the map.

------ Output ------ 

For each test case, output a single line containing the number of cells where monsters exist.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$1 ≤ R ≤ 50$
$1 ≤ C ≤ 50$

----- Sample Input 1 ------ 
2
5 5
^^^^^
^^^^^
^^^^#
^^^^^
^^^^^
5 7
^^#^^^^
^^#^#^#
#^^^^^^
^^#^^#^
^^^^^^^
----- Sample Output 1 ------ 
0
1
----- explanation 1 ------ 
Example case 1. There is no cell for which minimum of L, R, T, B is greater than some prime P.
Example case 2. The cell at [3, 4], (1-based indexing) is the only CPC.
"""

def count_monster_cells(test_cases):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    results = []
    
    for (R, C, grid) in test_cases:
        L_counts = [[0] * C for _ in range(R)]
        R_counts = [[0] * C for _ in range(R)]
        T_counts = [[0] * C for _ in range(R)]
        B_counts = [[0] * C for _ in range(R)]
        
        # Calculate L_counts and R_counts
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '^':
                    L_counts[i][j] = L_counts[i][j-1] + 1 if j > 0 else 1
                if grid[i][-j-1] == '^':
                    R_counts[i][-j-1] = R_counts[i][-j] + 1 if j > 0 else 1
        
        # Calculate T_counts and B_counts
        for j in range(C):
            for i in range(R):
                if grid[i][j] == '^':
                    T_counts[i][j] = T_counts[i-1][j] + 1 if i > 0 else 1
                if grid[-i-1][j] == '^':
                    B_counts[-i-1][j] = B_counts[-i][j] + 1 if i > 0 else 1
        
        monster_count = 0
        
        for i in range(1, R-1):
            for j in range(1, C-1):
                if grid[i][j] == '^':
                    min_LR = min(L_counts[i][j-1], R_counts[i][j+1])
                    min_TB = min(T_counts[i-1][j], B_counts[i+1][j])
                    min_val = min(min_LR, min_TB)
                    if any(is_prime(p) for p in range(2, min_val + 1)):
                        monster_count += 1
        
        results.append(monster_count)
    
    return results
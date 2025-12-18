"""
QUESTION:
Read problems statements in Mandarin Chinese  and Russian. 

Recently Chef bought a bunch of robot-waiters. And now he needs to know how much to pay for the electricity that robots use for their work. All waiters serve food from the kitchen (which is in the point (0, 0)) and carry it to some table (which is in some point (x, y)) in a shortest way. But this is a beta version of robots and they can only do the next moves: turn right and make a step forward or turn left and make a step forward. Initially they look in direction of X-axis. Your task is to calculate for each query the number of moves they’ll do to reach corresponding table.

------ Input ------ 

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows. For each test case there is a sing line containing two space-separated integers - x and y.

------ Output ------ 

For each test case, output a single line containing number of moves that robot will make to reach point (x, y)

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$-10^{9} ≤ x, y ≤ 10^{9}$
 
----- Sample Input 1 ------ 
2
3 3
3 4
----- Sample Output 1 ------ 
6
7

------ Explanation 0 ------ 

Example case 1. Sequence of moves would be LRLRLR
"""

def calculate_robot_moves(x: int, y: int) -> int:
    # Convert coordinates to their absolute values
    x = abs(x)
    y = abs(y)
    
    # Calculate the minimum of x and y
    z = min(x, y)
    
    # Reduce x and y by z
    x -= z
    y -= z
    
    # Calculate the remaining moves based on the remaining x and y
    if x == 0:
        if y % 2 != 0:
            res = 2 * y - 1
        else:
            res = 2 * y
    elif x % 2 != 0:
        res = 2 * x + 1
    else:
        res = 2 * x
    
    # Total moves is the sum of moves in the z direction and the remaining moves
    return 2 * z + res
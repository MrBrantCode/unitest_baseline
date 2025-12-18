"""
QUESTION:
Two countries, Country A and Country B, are at war. As a soldier in Country A, you will lead n soldiers to occupy the territory of Country B.

The territory of Country B is represented by a two-dimensional grid. The first place you occupy is a square on the 2D grid. Each of the soldiers you lead has h_i health. Each soldier can spend 1 health to move. Assuming that the current cell is (a, b), the movement destination is the four directions (a + 1, b), (a-1, b), (a, b + 1), (a, b-1). It is possible to choose. Soldiers will not be able to move from there when their health reaches zero. Any square passed by one or more soldiers can be occupied.

Your job is to find out how many squares you can occupy at most.
However, the size of this two-dimensional grid should be infinitely wide.



Input

The input is given in the following format.


n
h1
..
..
..
hn


Input meets the following constraints
1 ≤ n ≤ 500
1 ≤ hi ≤ 10,000,000

Output

Output the answer value on one line

Examples

Input

2
5
5


Output

11


Input

10
10
10
10
10
10
10
10
10
10
10


Output

93


Input

5
1
2
3
4
5


Output

15
"""

def max_occupied_squares(soldier_healths: list[int]) -> int:
    """
    Calculate the maximum number of squares that can be occupied by soldiers
    given their health values.

    Parameters:
    soldier_healths (list[int]): A list of integers where each integer represents
                                  the health of a soldier.

    Returns:
    int: The maximum number of squares that can be occupied.
    """
    # Sort the soldier healths in descending order
    sorted_healths = sorted(soldier_healths, reverse=True)
    
    # Initialize counters
    total_squares = 0
    current_level = 0
    
    # Calculate the maximum number of squares that can be occupied
    for health in sorted_healths:
        if health < current_level // 4:
            continue
        else:
            total_squares += health - current_level // 4
        current_level += 1
    
    # Return the total number of occupied squares plus the initial square
    return total_squares + 1
"""
QUESTION:
Problem

GPA is an abbreviation for "Galaxy Point of Aizu" and takes real numbers from 0 to 4.
GPA rock-paper-scissors is a game played by two people. After each player gives a signal of "rock-paper-scissors, pon (hoi)" to each other's favorite move, goo, choki, or par, the person with the higher GPA becomes the winner, and the person with the lower GPA becomes the loser. If they are the same, it will be a draw.

Since the GPA data of N people is given, output the points won in each round-robin battle.
However, the points won will be 3 when winning, 1 when drawing, and 0 when losing.

Round-robin is a system in which all participants play against participants other than themselves exactly once.

Constraints

The input satisfies the following conditions.

* 2 ≤ N ≤ 105
* N is an integer
* 0.000 ≤ ai ≤ 4.000 (1 ≤ i ≤ N)
* ai is a real number (1 ≤ i ≤ N)
* Each GPA is given up to 3 decimal places

Input

The input is given in the following format.


N
a1
a2
...
aN


The first line is given the number of people N to play GPA rock-paper-scissors.
The following N lines are given the data ai of the i-th person's GPA in one line.

Output

Output the points of the i-th person on the i-line on one line. (1 ≤ i ≤ N)

Examples

Input

3
1.000
3.000
3.000


Output

0
4
4


Input

3
1.000
2.000
3.000


Output

0
3
6
"""

def calculate_gpa_rps_scores(N, gpa_list):
    # Sort the GPA list to facilitate counting wins, draws, and losses
    sorted_gpa_list = sorted(gpa_list)
    
    # Initialize the result list to store the points for each person
    points = [0] * N
    
    # Calculate points for each person
    for i in range(N):
        gpa = gpa_list[i]
        
        # Count the number of people with a lower GPA (wins)
        wins = bisect.bisect_left(sorted_gpa_list, gpa)
        
        # Count the number of people with the same GPA (draws)
        draws = bisect.bisect_right(sorted_gpa_list, gpa) - wins - 1
        
        # Calculate the total points (3 points for each win, 1 point for each draw)
        points[i] = wins * 3 + draws
    
    return points
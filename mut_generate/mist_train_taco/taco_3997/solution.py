"""
QUESTION:
Ibis is fighting with a monster.
The health of the monster is H.
Ibis can cast N kinds of spells. Casting the i-th spell decreases the monster's health by A_i, at the cost of B_i Magic Points.
The same spell can be cast multiple times. There is no way other than spells to decrease the monster's health.
Ibis wins when the health of the monster becomes 0 or below.
Find the minimum total Magic Points that have to be consumed before winning.

-----Constraints-----
 - 1 \leq H \leq 10^4
 - 1 \leq N \leq 10^3
 - 1 \leq A_i \leq 10^4
 - 1 \leq B_i \leq 10^4
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
H N
A_1 B_1
:
A_N B_N

-----Output-----
Print the minimum total Magic Points that have to be consumed before winning.

-----Sample Input-----
9 3
8 3
4 2
2 1

-----Sample Output-----
4

First, let us cast the first spell to decrease the monster's health by 8, at the cost of 3 Magic Points. The monster's health is now 1.
Then, cast the third spell to decrease the monster's health by 2, at the cost of 1 Magic Point. The monster's health is now -1.
In this way, we can win at the total cost of 4 Magic Points.
"""

def minimum_magic_points(H, N, spells):
    # Initialize a list to store the minimum magic points required to reduce health to each possible value
    d = [float('inf')] * (H + 1)
    d[0] = 0  # No magic points needed to reduce health to 0
    
    # Iterate over each possible health value from 1 to H
    for i in range(1, H + 1):
        # For each health value, calculate the minimum magic points required
        for (A, B) in spells:
            if i - A >= 0:
                d[i] = min(d[i], d[i - A] + B)
            else:
                d[i] = min(d[i], B)  # If the spell can reduce health below 0, consider it as well
    
    return d[H]
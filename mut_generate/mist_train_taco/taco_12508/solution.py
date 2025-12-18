"""
QUESTION:
Takahashi lives in another world. There are slimes (creatures) of 10000 colors in this world. Let us call these colors Color 1, 2, ..., 10000.

Takahashi has N slimes, and they are standing in a row from left to right. The color of the i-th slime from the left is a_i. If two slimes of the same color are adjacent, they will start to combine themselves. Because Takahashi likes smaller slimes, he has decided to change the colors of some of the slimes with his magic.

Takahashi can change the color of one slime to any of the 10000 colors by one spell. How many spells are required so that no slimes will start to combine themselves?

Constraints

* 2 \leq N \leq 100
* 1 \leq a_i \leq N
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N
a_1 a_2 ... a_N


Output

Print the minimum number of spells required.

Examples

Input

5
1 1 2 2 2


Output

2


Input

3
1 2 1


Output

0


Input

5
1 1 1 1 1


Output

2


Input

14
1 2 2 3 3 3 4 4 4 4 1 2 3 4


Output

4
"""

def min_spells_to_prevent_combining(N, slimes):
    spells = 0
    for i in range(1, N):
        if slimes[i] == slimes[i - 1]:
            slimes[i] = 0  # Marking the slime as changed (0 is an arbitrary choice)
            spells += 1
    return spells
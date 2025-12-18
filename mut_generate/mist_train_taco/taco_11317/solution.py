"""
QUESTION:
Balph is learning to play a game called Buma. In this game, he is given a row of colored balls. He has to choose the color of one new ball and the place to insert it (between two balls, or to the left of all the balls, or to the right of all the balls).

When the ball is inserted the following happens repeatedly: if some segment of balls of the same color became longer as a result of a previous action and its length became at least 3, then all the balls of this segment are eliminated. 

Consider, for example, a row of balls 'AAABBBWWBB'. Suppose Balph chooses a ball of color 'W' and the place to insert it after the sixth ball, i. e. to the left of the two 'W's. After Balph inserts this ball, the balls of color 'W' are eliminated, since this segment was made longer and has length 3 now, so the row becomes 'AAABBBBB'. The balls of color 'B' are eliminated now, because the segment of balls of color 'B' became longer and has length 5 now. Thus, the row becomes 'AAA'. However, none of the balls are eliminated now, because there is no elongated segment.

Help Balph count the number of possible ways to choose a color of a new ball and a place to insert it that leads to the elimination of all the balls.

Input

The only line contains a non-empty string of uppercase English letters of length at most 3 ⋅ 10^5. Each letter represents a ball with the corresponding color.

Output

Output the number of ways to choose a color and a position of a new ball in order to eliminate all the balls.

Examples

Input


BBWWBB


Output


3


Input


BWWB


Output


0


Input


BBWBB


Output


0


Input


OOOWWW


Output


0


Input


WWWOOOOOOWWW


Output


7
"""

def count_elimination_ways(balls: str) -> int:
    n = len(balls)
    condensed = []
    temp = balls[0]
    count = 1
    
    # Condense the string into segments of same color balls
    for i in range(1, n):
        if balls[i] == temp:
            count += 1
        else:
            condensed.append((temp, count))
            temp = balls[i]
            count = 1
    condensed.append((temp, count))
    
    # Check if the condensed list can be symmetrically eliminated
    if len(condensed) % 2 == 0:
        return 0
    elif condensed[int((len(condensed) - 1) / 2)][1] < 2:
        return 0
    else:
        for i in range(int((len(condensed) - 1) / 2)):
            if condensed[i][0] != condensed[-i - 1][0]:
                return 0
            elif condensed[i][1] + condensed[-i - 1][1] < 3:
                return 0
        return condensed[int((len(condensed) - 1) / 2)][1] + 1
"""
QUESTION:
Problem Statement

Mr. Takatsuki, who is planning to participate in the Aizu training camp, has a poor house and always tries to save as much paper as possible. She decided to play a ghost leg with other participants to decide the team for the Aizu training camp.

How to make Amidakuji for this training camp is as follows. First, write N vertical bars in parallel on the paper. Then, write the M horizontal bars in order from the top so that they are perpendicular to the vertical bars and the heights of the horizontal bars are all different. For example, the Amida of Sample Input 1 is as shown in Fig. 1.

Here, Mr. Takatsuki, a little dissatisfied expression. It's a waste of paper to write a ghost leg so vertically. You should be able to compress the height more. So, I want her to solve the problem of height compression of Amidakuji shown below.

First, the height of the Amidakuji is the value obtained by counting the horizontal bars that exist at the same height together as the height 1 and counting this to the bottom horizontal bar. Here, it is assumed that each horizontal bar can be freely moved up and down in order to perform height compression. However, it is not permissible to remove or add horizontal bars. The Amidakuji after height compression must meet the following conditions.

* The end points of the horizontal bar do not touch the end points of other horizontal bars.
* The result of tracing the Amidakuji after compression and the result of tracing the Amidakuji before compression match.



FIG. 2 is a compressed version of FIG. The "horizontal bar connecting vertical bars 1 and 2" moves to the top and becomes the same height as the "horizontal bar connecting vertical bars 4 and 5", and these two are height 1. After that, the "horizontal bar connecting the vertical bars 3 and 4" and the "horizontal bar connecting the vertical bars 2 and 3" have different heights, and the total height is 3.

<image>

Compress the height of the given Amidakuji and output the compressed height.

Constraints

* 2 <= N <= 8
* 1 <= M <= 8
* 1 <= ai <= N --1

Input

Each data set is input in the following format.


N M
a1
a2
...
aM


All inputs are integers. N indicates the number of vertical bars and M indicates the number of horizontal bars. Then, the information of the horizontal bar is input over M lines. ai indicates that the i-th horizontal bar connects the vertical bar ai and the vertical bar to the right of it. The i-th horizontal bar exists above the i + 1-th horizontal bar.

Output

Outputs the height of the compressed Amidakuji in one line.

Examples

Input

5 4
4
3
1
2


Output

3


Input

4 3
1
2
3


Output

3
"""

from itertools import permutations

def compress_amidakuji(N, M, horizontal_bars):
    # Convert horizontal_bars to 0-indexed
    k = [bar - 1 for bar in horizontal_bars]
    
    # Initial state of the vertical bars
    g = [i for i in range(N)]
    
    # Apply the original horizontal bars to the initial state
    for i in range(N):
        for j in k:
            if g[i] == j:
                g[i] = j + 1
            elif g[i] == j + 1:
                g[i] = j
    
    # Initialize the minimum height to a large number
    s = 10
    
    # Try all permutations of the horizontal bars
    for K in permutations(k):
        G = [i for i in range(N)]
        
        # Apply the current permutation of horizontal bars
        for i in range(N):
            for j in K:
                if G[i] == j:
                    G[i] = j + 1
                elif G[i] == j + 1:
                    G[i] = j
        
        # If the result after applying the permutation does not match the original, skip this permutation
        if G != g:
            continue
        
        # Calculate the height of the Amidakuji for the current permutation
        l = [0] * N
        for i in range(M):
            a = K[i]
            b = max(l[a], l[a + 1])
            l[a] = b + 1
            l[a + 1] = b + 1
        
        # Update the minimum height
        s = min(s, max(l))
    
    return s
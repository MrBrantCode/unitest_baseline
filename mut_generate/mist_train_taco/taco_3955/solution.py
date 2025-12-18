"""
QUESTION:
problem

Prepare the Othello board. The upper left is $ (1,1) $ and the lower right is $ (8,8) $. The board to be prepared here is $ (5,4) as follows. ) There is no $ black stone.


........
........
........
... ox ...
.... o ...
........
........
........


Kuroishi: x Shiraishi: o
8x8 board
From this state, Black starts Othello first.

AOR Ika-chan plays $ q $ times according to the following rules.

A rectangular area is given, with the upper left as the cell in the $ a $ and $ b $ columns, and the lower right as the cell in the $ c $ and $ d $ columns.

AOR Ika-chan puts black stones and white stones alternately according to the rules of Othello (reference: Wikipedia Othello) so as to maximize the number of stones contained in this rectangular area.
When no more stones can be placed (when both Shiraishi and Kuroishi have to pass or when all the boards are filled), the game ends.

In each game, output the number of stones when the number of stones contained in the area is maximized.
Since the number of inputs and outputs may increase, it is recommended to use high-speed functions for input and output.



output

In each game, output the number of stones in the area when the number of stones is maximized. Also, output a line break at the end.

Example

Input

3
1 1 8 8
2 4 3 8
8 8 8 8


Output

48
7
1
"""

def calculate_max_stones(q, queries):
    results = []
    for i in range(q):
        (a, b, c, d) = queries[i]
        ans = 0
        for j in range(a, c + 1):
            for k in range(b, d + 1):
                ans += 0 if j % 2 == 1 and k % 2 == 0 else 1
        results.append(ans)
    return results
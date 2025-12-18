"""
QUESTION:
Alperen is standing at the point $(0,0)$. He is given a string $s$ of length $n$ and performs $n$ moves. The $i$-th move is as follows:

if $s_i = {L}$, then move one unit left;

if $s_i = {R}$, then move one unit right;

if $s_i = {U}$, then move one unit up;

if $s_i = {D}$, then move one unit down.

If Alperen starts at the center point, he can make the four moves shown.

There is a candy at $(1,1)$ (that is, one unit above and one unit to the right of Alperen's starting point). You need to determine if Alperen ever passes the candy.

Alperen's path in the first test case.


-----Input-----

The first line of the input contains an integer $t$ ($1 \leq t \leq 1000$) — the number of testcases.

The first line of each test case contains an integer $n$ ($1 \leq n \leq 50$) — the length of the string.

The second line of each test case contains a string $s$ of length $n$ consisting of characters ${L}$, ${R}$, ${D}$, and ${U}$, denoting the moves Alperen makes.


-----Output-----

For each test case, output "YES" (without quotes) if Alperen passes the candy, and "NO" (without quotes) otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).


-----Examples-----

Input
7
7
UUURDDL
2
UR
8
RRRUUDDD
3
LLL
4
DUUR
5
RUDLL
11
LLLLDDRUDRD
Output
YES
YES
NO
NO
YES
YES
NO


-----Note-----

In the first test case, Alperen follows the path $$(0,0) \overset{{U}}{\to} (0,1) \overset{{U}}{\to} (0,2) \overset{{U}}{\to} (0,3) \overset{{R}}{\to} (1,3) \overset{{D}}{\to} (1,2) \overset{{D}}{\to} \color{green}{\mathbf{(1,1)}} \overset{{L}}{\to} (0,1).$$ Note that Alperen doesn't need to end at the candy's location of $(1,1)$, he just needs to pass it at some point.

In the second test case, Alperen follows the path $$(0,0) \overset{{U}}{\to} (0,1) \overset{{R}}{\to} \color{green}{\mathbf{(1,1)}}.$$

In the third test case, Alperen follows the path $$(0,0) \overset{{R}}{\to} (1,0) \overset{{R}}{\to} (2,0) \overset{{R}}{\to} (3,0) \overset{{U}}{\to} (3,1) \overset{{U}}{\to} (3,2) \overset{{D}}{\to} (3,1) \overset{{D}}{\to} (3,0) \overset{{D}}{\to} (3,-1).$$

In the fourth test case, Alperen follows the path $$(0,0) \overset{{L}}{\to} (-1,0) \overset{{L}}{\to} (-2,0) \overset{{L}}{\to} (-3,0).$$
"""

def passes_candy(s: str, n: int) -> bool:
    x, y = 0, 0
    candy_x, candy_y = 1, 1
    
    for move in s:
        if move == 'L':
            x -= 1
        elif move == 'R':
            x += 1
        elif move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        
        if x == candy_x and y == candy_y:
            return True
    
    return False
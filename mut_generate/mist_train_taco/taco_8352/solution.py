"""
QUESTION:
There is an infinite board of square tiles. Initially all tiles are white.

Vova has a red marker and a blue marker. Red marker can color $a$ tiles. Blue marker can color $b$ tiles. If some tile isn't white then you can't use marker of any color on it. Each marker must be drained completely, so at the end there should be exactly $a$ red tiles and exactly $b$ blue tiles across the board.

Vova wants to color such a set of tiles that:

  they would form a rectangle, consisting of exactly $a+b$ colored tiles;  all tiles of at least one color would also form a rectangle. 

Here are some examples of correct colorings:

 [Image] 

Here are some examples of incorrect colorings:

 [Image] 

Among all correct colorings Vova wants to choose the one with the minimal perimeter. What is the minimal perimeter Vova can obtain?

It is guaranteed that there exists at least one correct coloring.


-----Input-----

A single line contains two integers $a$ and $b$ ($1 \le a, b \le 10^{14}$) — the number of tiles red marker should color and the number of tiles blue marker should color, respectively.


-----Output-----

Print a single integer — the minimal perimeter of a colored rectangle Vova can obtain by coloring exactly $a$ tiles red and exactly $b$ tiles blue.

It is guaranteed that there exists at least one correct coloring.


-----Examples-----
Input
4 4

Output
12

Input
3 9

Output
14

Input
9 3

Output
14

Input
3 6

Output
12

Input
506 2708

Output
3218



-----Note-----

The first four examples correspond to the first picture of the statement.

Note that for there exist multiple correct colorings for all of the examples.

In the first example you can also make a rectangle with sides $1$ and $8$, though its perimeter will be $18$ which is greater than $8$.

In the second example you can make the same resulting rectangle with sides $3$ and $4$, but red tiles will form the rectangle with sides $1$ and $3$ and blue tiles will form the rectangle with sides $3$ and $3$.
"""

def minimal_perimeter_of_colored_rectangle(a: int, b: int) -> int:
    import math
    
    s1 = math.isqrt(a)
    s2 = math.isqrt(b)
    s3 = math.isqrt(a + b)
    
    m = a + b
    ans = 0
    
    for i in range(1, s3 + 1):
        if i <= s1 and a % i == 0:
            m = min(m, a // i)
        if i <= s2 and b % i == 0:
            m = min(m, b // i)
        if (a + b) % i == 0:
            d = (a + b) // i
            if d >= m:
                ans = (i + d) * 2
    
    return ans
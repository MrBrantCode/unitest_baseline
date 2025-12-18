"""
QUESTION:
You a captain of a ship. Initially you are standing in a point $(x_1, y_1)$ (obviously, all positions in the sea can be described by cartesian plane) and you want to travel to a point $(x_2, y_2)$. 

You know the weather forecast — the string $s$ of length $n$, consisting only of letters U, D, L and R. The letter corresponds to a direction of wind. Moreover, the forecast is periodic, e.g. the first day wind blows to the side $s_1$, the second day — $s_2$, the $n$-th day — $s_n$ and $(n+1)$-th day — $s_1$ again and so on. 

Ship coordinates change the following way:  if wind blows the direction U, then the ship moves from $(x, y)$ to $(x, y + 1)$;  if wind blows the direction D, then the ship moves from $(x, y)$ to $(x, y - 1)$;  if wind blows the direction L, then the ship moves from $(x, y)$ to $(x - 1, y)$;  if wind blows the direction R, then the ship moves from $(x, y)$ to $(x + 1, y)$. 

The ship can also either go one of the four directions or stay in place each day. If it goes then it's exactly 1 unit of distance. Transpositions of the ship and the wind add up. If the ship stays in place, then only the direction of wind counts. For example, if wind blows the direction U and the ship moves the direction L, then from point $(x, y)$ it will move to the point $(x - 1, y + 1)$, and if it goes the direction U, then it will move to the point $(x, y + 2)$.

You task is to determine the minimal number of days required for the ship to reach the point $(x_2, y_2)$.


-----Input-----

The first line contains two integers $x_1, y_1$ ($0 \le x_1, y_1 \le 10^9$) — the initial coordinates of the ship.

The second line contains two integers $x_2, y_2$ ($0 \le x_2, y_2 \le 10^9$) — the coordinates of the destination point.

It is guaranteed that the initial coordinates and destination point coordinates are different.

The third line contains a single integer $n$ ($1 \le n \le 10^5$) — the length of the string $s$.

The fourth line contains the string $s$ itself, consisting only of letters U, D, L and R.


-----Output-----

The only line should contain the minimal number of days required for the ship to reach the point $(x_2, y_2)$.

If it's impossible then print "-1".


-----Examples-----
Input
0 0
4 6
3
UUU

Output
5

Input
0 3
0 0
3
UDD

Output
3

Input
0 0
0 1
1
L

Output
-1



-----Note-----

In the first example the ship should perform the following sequence of moves: "RRRRU". Then its coordinates will change accordingly: $(0, 0)$ $\rightarrow$ $(1, 1)$ $\rightarrow$ $(2, 2)$ $\rightarrow$ $(3, 3)$ $\rightarrow$ $(4, 4)$ $\rightarrow$ $(4, 6)$.

In the second example the ship should perform the following sequence of moves: "DD" (the third day it should stay in place). Then its coordinates will change accordingly: $(0, 3)$ $\rightarrow$ $(0, 3)$ $\rightarrow$ $(0, 1)$ $\rightarrow$ $(0, 0)$.

In the third example the ship can never reach the point $(0, 1)$.
"""

def minimal_days_to_reach_destination(start_x, start_y, dest_x, dest_y, wind_pattern):
    def count_wind(k, wind):
        n = len(wind)
        full_x = sum((x for (x, y) in wind))
        full_y = sum((y for (x, y) in wind))
        full = k // n
        part = k % n
        part_x = sum((x for (x, y) in wind[:part]))
        part_y = sum((y for (x, y) in wind[:part]))
        return (full * full_x + part_x, full * full_y + part_y)

    def f(k, start, fin, wind):
        vector_sum = count_wind(k, wind)
        x_i = start[0] + vector_sum[0] - fin[0]
        y_i = start[1] + vector_sum[1] - fin[1]
        return abs(x_i) + abs(y_i) <= k

    coords = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    wind = [coords[i] for i in wind_pattern]
    left = 1
    right = 2 * 10**15 + 1
    
    while left != right:
        middle = (left + right) // 2
        if f(middle, (start_x, start_y), (dest_x, dest_y), wind) < 1:
            left = middle + 1
        else:
            right = middle
    
    if left == 2 * 10**15 + 1:
        return -1
    
    return left
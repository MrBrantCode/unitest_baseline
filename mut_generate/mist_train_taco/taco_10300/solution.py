"""
QUESTION:
There are $n$ points on a coordinate axis $OX$. The $i$-th point is located at the integer point $x_i$ and has a speed $v_i$. It is guaranteed that no two points occupy the same coordinate. All $n$ points move with the constant speed, the coordinate of the $i$-th point at the moment $t$ ($t$ can be non-integer) is calculated as $x_i + t \cdot v_i$.

Consider two points $i$ and $j$. Let $d(i, j)$ be the minimum possible distance between these two points over any possible moments of time (even non-integer). It means that if two points $i$ and $j$ coincide at some moment, the value $d(i, j)$ will be $0$.

Your task is to calculate the value $\sum\limits_{1 \le i < j \le n}$ $d(i, j)$ (the sum of minimum distances over all pairs of points).


-----Input-----

The first line of the input contains one integer $n$ ($2 \le n \le 2 \cdot 10^5$) — the number of points.

The second line of the input contains $n$ integers $x_1, x_2, \dots, x_n$ ($1 \le x_i \le 10^8$), where $x_i$ is the initial coordinate of the $i$-th point. It is guaranteed that all $x_i$ are distinct.

The third line of the input contains $n$ integers $v_1, v_2, \dots, v_n$ ($-10^8 \le v_i \le 10^8$), where $v_i$ is the speed of the $i$-th point.


-----Output-----

Print one integer — the value $\sum\limits_{1 \le i < j \le n}$ $d(i, j)$ (the sum of minimum distances over all pairs of points).


-----Examples-----
Input
3
1 3 2
-100 2 3

Output
3

Input
5
2 1 4 3 5
2 2 2 3 4

Output
19

Input
2
2 1
-3 0

Output
0
"""

def calculate_minimum_distance_sum(n, x, v):
    """
    Calculate the sum of the minimum distances over all pairs of points.

    Parameters:
    n (int): The number of points.
    x (list of int): The list of initial coordinates of the points.
    v (list of int): The list of speeds of the points.

    Returns:
    int: The sum of the minimum distances over all pairs of points.
    """
    from bisect import bisect_left
    
    # Pair the speeds and coordinates, then sort by speed
    z = sorted(list(zip(v, x)))
    
    # Sort the coordinates
    x.sort()
    
    # Initialize the sum
    s = 0
    
    # Calculate the sum of minimum distances
    for i in range(n):
        s += (bisect_left(x, z[i][1]) + i - n + 1) * z[i][1]
    
    return s
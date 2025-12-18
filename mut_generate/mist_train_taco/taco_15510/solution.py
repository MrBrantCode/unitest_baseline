"""
QUESTION:
The numbers $1, \, 2, \, \dots, \, n \cdot k$ are colored with $n$ colors. These colors are indexed by $1, \, 2, \, \dots, \, n$. For each $1 \le i \le n$, there are exactly $k$ numbers colored with color $i$.

Let $[a, \, b]$ denote the interval of integers between $a$ and $b$ inclusive, that is, the set $\{a, \, a + 1, \, \dots, \, b\}$. You must choose $n$ intervals $[a_1, \, b_1], \, [a_2, \, b_2], \, \dots, [a_n, \, b_n]$ such that:

for each $1 \le i \le n$, it holds $1 \le a_i < b_i \le n \cdot k$;

for each $1 \le i \le n$, the numbers $a_i$ and $b_i$ are colored with color $i$;

each number $1 \le x \le n \cdot k$ belongs to at most $\left\lceil \frac{n}{k - 1} \right\rceil$ intervals.

One can show that such a family of intervals always exists under the given constraints.


-----Input-----

The first line contains two integers $n$ and $k$ ($1 \le n \le 100$, $2 \le k \le 100$) — the number of colors and the number of occurrences of each color.

The second line contains $n \cdot k$ integers $c_1, \, c_2, \, \dots, \, c_{nk}$ ($1 \le c_j \le n$), where $c_j$ is the color of number $j$. It is guaranteed that, for each $1 \le i \le n$, it holds $c_j = i$ for exactly $k$ distinct indices $j$.


-----Output-----

Output $n$ lines. The $i$-th line should contain the two integers $a_i$ and $b_i$.

If there are multiple valid choices of the intervals, output any.


-----Examples-----

Input
4 3
2 4 3 1 1 4 2 3 2 1 3 4
Output
4 5
1 7
8 11
6 12
Input
1 2
1 1
Output
1 2
Input
3 3
3 1 2 3 2 1 2 1 3
Output
6 8
3 7
1 4
Input
2 3
2 1 1 1 2 2
Output
2 3
5 6


-----Note-----

In the first sample, each number can be contained in at most $\left\lceil \frac{4}{3 - 1} \right\rceil = 2$ intervals. The output is described by the following picture:

In the second sample, the only interval to be chosen is forced to be $[1, \, 2]$, and each number is indeed contained in at most $\left\lceil \frac{1}{2 - 1} \right\rceil = 1$ interval.

In the third sample, each number can be contained in at most $\left\lceil \frac{3}{3 - 1} \right\rceil = 2$ intervals. The output is described by the following picture:
"""

def find_color_intervals(n, k, colors):
    """
    Finds n intervals [a_i, b_i] such that:
    - For each 1 ≤ i ≤ n, 1 ≤ a_i < b_i ≤ n * k.
    - For each 1 ≤ i ≤ n, the numbers a_i and b_i are colored with color i.
    - Each number 1 ≤ x ≤ n * k belongs to at most ceil(n / (k - 1)) intervals.

    Parameters:
    - n (int): The number of colors.
    - k (int): The number of occurrences of each color.
    - colors (list[int]): A list of integers representing the colors of the numbers from 1 to n * k.

    Returns:
    - list[tuple[int, int]]: A list of tuples, where each tuple represents the interval [a_i, b_i] for each color i.
    """
    # Adjust colors to be zero-indexed
    colors = [color - 1 for color in colors]
    
    # Initialize a list to store the positions of each color
    color_positions = [[] for _ in range(n)]
    
    # Populate the color_positions list
    for index, color in enumerate(colors):
        color_positions[color].append(index)
    
    # Initialize a list to track which colors have been used
    used_colors = [0] * n
    
    # Calculate the number of intervals each color can be part of
    q = n // (k - 1)
    r = n % (k - 1)
    
    # Initialize a list to store the result intervals
    result_intervals = [0] * n
    
    # Calculate the intervals
    for i in range(1, k):
        a = []
        c = q + (i <= r)
        for j in range(n):
            if used_colors[j] == 0:
                a.append((color_positions[j][i], j))
        a = sorted(a)[:c]
        for (x, ind) in a:
            used_colors[ind] = 1
            result_intervals[ind] = (color_positions[ind][i - 1] + 1, color_positions[ind][i] + 1)
    
    return result_intervals
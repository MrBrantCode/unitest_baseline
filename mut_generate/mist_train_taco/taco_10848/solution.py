"""
QUESTION:
Vasya works as a watchman in the gallery. Unfortunately, one of the most expensive paintings was stolen while he was on duty. He doesn't want to be fired, so he has to quickly restore the painting. He remembers some facts about it.  The painting is a square 3 × 3, each cell contains a single integer from 1 to n, and different cells may contain either different or equal integers.  The sum of integers in each of four squares 2 × 2 is equal to the sum of integers in the top left square 2 × 2.  Four elements a, b, c and d are known and are located as shown on the picture below. $\left. \begin{array}{|c|c|c|} \hline ? & {a} & {?} \\ \hline b & {?} & {c} \\ \hline ? & {d} & {?} \\ \hline \end{array} \right.$

Help Vasya find out the number of distinct squares the satisfy all the conditions above. Note, that this number may be equal to 0, meaning Vasya remembers something wrong.

Two squares are considered to be different, if there exists a cell that contains two different integers in different squares.


-----Input-----

The first line of the input contains five integers n, a, b, c and d (1 ≤ n ≤ 100 000, 1 ≤ a, b, c, d ≤ n) — maximum possible value of an integer in the cell and four integers that Vasya remembers.


-----Output-----

Print one integer — the number of distinct valid squares.


-----Examples-----
Input
2 1 1 1 2

Output
2

Input
3 3 1 2 3

Output
6



-----Note-----

Below are all the possible paintings for the first sample. $\left. \begin{array}{|l|l|l|} \hline 2 & {1} & {2} \\ \hline 1 & {1} & {1} \\ \hline 1 & {2} & {1} \\ \hline \end{array} \right.$ $\left. \begin{array}{|l|l|l|} \hline 2 & {1} & {2} \\ \hline 1 & {2} & {1} \\ \hline 1 & {2} & {1} \\ \hline \end{array} \right.$

In the second sample, only paintings displayed below satisfy all the rules. $\left. \begin{array}{|c|c|c|} \hline 2 & {3} & {1} \\ \hline 1 & {1} & {2} \\ \hline 2 & {3} & {1} \\ \hline \end{array} \right.$ $\left. \begin{array}{|c|c|c|} \hline 2 & {3} & {1} \\ \hline 1 & {2} & {2} \\ \hline 2 & {3} & {1} \\ \hline \end{array} \right.$ $\left. \begin{array}{|l|l|l|} \hline 2 & {3} & {1} \\ \hline 1 & {3} & {2} \\ \hline 2 & {3} & {1} \\ \hline \end{array} \right.$ $\left. \begin{array}{|c|c|c|} \hline 3 & {3} & {2} \\ \hline 1 & {1} & {2} \\ \hline 3 & {3} & {2} \\ \hline \end{array} \right.$ $\left. \begin{array}{|c|c|c|} \hline 3 & {3} & {2} \\ \hline 1 & {2} & {2} \\ \hline 3 & {3} & {2} \\ \hline \end{array} \right.$ $\left. \begin{array}{|c|c|c|} \hline 3 & {3} & {2} \\ \hline 1 & {3} & {2} \\ \hline 3 & {3} & {2} \\ \hline \end{array} \right.$
"""

def count_distinct_squares(n: int, a: int, b: int, c: int, d: int) -> int:
    """
    Counts the number of distinct 3x3 squares that satisfy the given conditions.

    Parameters:
    n (int): The maximum possible value of an integer in the cell (1 ≤ n ≤ 100000).
    a (int): Integer in the top middle cell.
    b (int): Integer in the middle left cell.
    c (int): Integer in the bottom middle cell.
    d (int): Integer in the middle right cell.

    Returns:
    int: The number of distinct valid squares.
    """
    ans = 0
    for x in range(1, n + 1):
        y = x + b - c
        z = x + a - d
        w = a + y - d
        if 1 <= y <= n and 1 <= z <= n and 1 <= w <= n:
            ans += 1
    return ans * n
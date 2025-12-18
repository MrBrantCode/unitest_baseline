"""
QUESTION:
F: Grid number

problem

Ebi-chan is trying to write exactly one integer from 1 to 2 \ times n in a grid with n columns horizontally and 2 rows vertically.

Only one integer can be written to each cell in the grid.

It's not fun just to write normally, so I set the following rules.

* The absolute value of the difference between the integers written in two adjacent cells is less than or equal to k.
* When there is a cell to the right of a cell, the integer written to the cell is truly smaller than the integer written to the cell to the right.
* When there is a cell under a cell, the integer written in the cell is truly smaller than the integer written in the cell below.



Here, two adjacent squares represent squares that share the top, bottom, left, and right sides with a certain square.

How many ways to write this? The answer can be very large, so print the remainder after dividing by the prime number m.

Supplement

The second and third rules above require you to write an integer so that it doesn't violate the inequality sign, as shown in the figure below.

<image>

Input format

You will be given three integers as input.


n k m

Constraint

* 1 \ leq n \ leq 100
* 1 \ leq k \ leq 10
* 2 \ leq m \ leq 10 ^ 9 + 7
* m is a prime number



Output format

Please output the number on one line according to how to write the number. Also, be careful not to forget the trailing line break.

Input example 1


3 2 7

Output example 1


1

<image>

* The above writing method meets the conditions, and there is no other writing method that meets the conditions.



Input example 2


5 10 11

Output example 2


9

* Output the remainder divided by m.





Example

Input

3 2 7


Output

1
"""

from collections import Counter

def count_valid_grid_configurations(n, k, m):
    dp = [Counter() for _ in range(2 * n)]
    dp[0][None, (0,)] = 1
    
    for i in range(2 * n - 1):
        for ((left, top), v) in dp[i].items():
            if len(top) > k + 1:
                continue
            if left == None:
                if top and i + 1 - top[0] <= k:
                    dp[i + 1][i + 1, top] = (dp[i + 1][i + 1, top] + v) % m
            elif i + 1 - left <= k and len(top) > 1 and (i + 1 - top[1] <= k):
                dp[i + 1][i + 1, top[1:]] = (dp[i + 1][i + 1, top[1:]] + v) % m
            if top and i + 1 - top[-1] <= k:
                top = list(top)
                top.append(i + 1)
                top = tuple(top)
                dp[i + 1][left, top] = (dp[i + 1][left, top] + v) % m
    
    res = 0
    for ((left, top), v) in dp[2 * n - 1].items():
        if len(top) == 1:
            assert left == 2 * n - 1
            res = (res + v) % m
    
    return res
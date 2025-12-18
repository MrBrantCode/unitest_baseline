"""
QUESTION:
Given an array $a$ of length $n$ and an integer $k$, you are tasked to find any two numbers $l$ and $r$ ($l \leq r$) such that:

For each $x$ $(l \leq x \leq r)$, $x$ appears in $a$ at least $k$ times (i.e. $k$ or more array elements are equal to $x$).

The value $r-l$ is maximized.

If no numbers satisfy the conditions, output -1.

For example, if $a=[11, 11, 12, 13, 13, 14, 14]$ and $k=2$, then:

for $l=12$, $r=14$ the first condition fails because $12$ does not appear at least $k=2$ times.

for $l=13$, $r=14$ the first condition holds, because $13$ occurs at least $k=2$ times in $a$ and $14$ occurs at least $k=2$ times in $a$.

for $l=11$, $r=11$ the first condition holds, because $11$ occurs at least $k=2$ times in $a$.

A pair of $l$ and $r$ for which the first condition holds and $r-l$ is maximal is $l = 13$, $r = 14$.


-----Input-----

The first line of the input contains a single integer $t$ ($1 \le t \le 1000$) — the number of test cases. The description of test cases follows.

The first line of each test case contains the integers $n$ and $k$ ($1 \le n \le 2 \cdot 10^5$, $1 \leq k \leq n$) — the length of the array $a$ and the minimum amount of times each number in the range $[l, r]$ should appear respectively.

Then a single line follows, containing $n$ integers describing the array $a$ ($1 \leq a_i \leq 10^9$).

It is guaranteed that the sum of $n$ over all test cases does not exceed $2 \cdot 10^5$.


-----Output-----

For each test case output $2$ numbers, $l$ and $r$ that satisfy the conditions, or "-1" if no numbers satisfy the conditions.

If multiple answers exist, you can output any.


-----Examples-----

Input
4
7 2
11 11 12 13 13 14 14
5 1
6 3 5 2 1
6 4
4 3 4 3 3 4
14 2
1 1 2 2 2 3 3 3 3 4 4 4 4 4
Output
13 14
1 3
-1
1 4


-----Note-----

None
"""

from collections import Counter

def find_max_range(a, k):
    """
    Finds the maximum range [l, r] such that for each x (l <= x <= r), x appears in a at least k times.
    
    Parameters:
    a (list of int): The array of integers.
    k (int): The minimum number of times each number in the range [l, r] should appear.
    
    Returns:
    tuple: A tuple (l, r) representing the indices l and r that satisfy the conditions, or -1 if no such indices exist.
    """
    a = sorted(a)
    counter = Counter(a)
    l, r, target_l, my_max = -1, -1, -1, -1
    
    for val in counter:
        if counter[val] < k:
            continue
        if val == r + 1:
            r = val
            if val - l > my_max:
                my_max, target_l = val - l, l
        else:
            l, r = val, val
            if my_max == -1:
                my_max, target_l = 0, l
    
    if my_max != -1:
        return (target_l, target_l + my_max)
    else:
        return -1